import re
from datetime import datetime
from src.line_type import LineType


class Line:

    def __init__(self, text: str):
        self.text = text
        self.type = self.detect_line_type(text)
        self.content = self.get_line_content()

    def detect_line_type(self, text: str) -> LineType:
        date_pattern = r"(\d{4})\.(\d{2})\.(\d{2}) [月火水木金土日]曜日"
        header_pattern = r"(\d{1,2}):(\d{2}) (.+) (.+)"
        self.date_match = re.search(date_pattern, text)
        self.header_match = re.search(header_pattern, text)
        if self.date_match:
            return LineType.DATE
        elif self.header_match:
            return LineType.HEADER
        else:
            return LineType.OTHER

    def get_line_content(self):
        if self.date_match:
            year, month, day = int(self.date_match.group(1)), int(
                self.date_match.group(2)), int(self.date_match.group(3))
            return datetime(year, month, day)
        elif self.header_match:
            hour, minute, user, first_message_body = int(
                self.header_match.group(1)), int(self.header_match.group(
                    2)), self.header_match.group(3), self.header_match.group(4)
            return hour, minute, user, first_message_body
        else:
            return self.text
