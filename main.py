from src.data_file import DataFile


def main():
    file_path = "data/test_talk.txt"
    data_file = DataFile(file_path)
    for message in data_file.messages:
        if message.datetime.hour == 14 and message.datetime.minute == 40:
            print(message.content)
     


if __name__ == '__main__':
    main()