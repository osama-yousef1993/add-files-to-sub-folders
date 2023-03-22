from helpers.check_folders import Helper
import os
import shutil


class FolderProcess():
    def __init__(self):
        self.handler = Helper()
        self.folders_list = self.handler.create_languages_folders()

    def process(self):
        files_name = os.listdir("files/")
        for folder in self.folders_list:
            for file in files_name:
                name = file.split("-")[0]
                if name == folder:
                    shutil.move(f"files/{file}", f"files/{folder}")
