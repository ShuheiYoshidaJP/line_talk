from datetime import datetime, time


class Message():

    def __init__(self, *args):
        datetime, hour, minute, user, first = args
        self.datetime = datetime.combine(datetime.date(),
                                         time(hour=hour, minute=minute))
        self.user = user
        self.content = first + '\n'
        

    def set_other(self, message: str):
        if self.content == None:
            ValueError("すでにヘッダーラインにおいてボディが存在するはずです。")
        else:
            self.content += message
