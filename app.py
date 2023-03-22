from handler.process import FolderProcess


def main():
    handler = FolderProcess()
    handler.process()
    del handler


if __name__ == '__main__':
    main()
