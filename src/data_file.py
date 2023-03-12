from datetime import datetime
from typing import List
from src.line import Line
from src.line_type import LineType
from src.message import Message


class DataFile():

    def __init__(self, file_path):
        self.messages = self.read_file(file_path)

    def read_file(self, file_path):
        messages: List[Message] = []
        datelist: List[datetime] = []
        with open(file_path, "r") as file:
            lines_str = file.readlines()
        for text in lines_str:
            line = Line(text)
            if line.type == LineType.DATE:
                datelist.append(line.content)  # type: ignore
            elif line.type == LineType.TIME:
                args = (datelist[-1], ) + line.content  # type: ignore
                messages.append(Message(*args))
            else:
                messages[-1].set_other(line.content)  # type: ignore
        return messages