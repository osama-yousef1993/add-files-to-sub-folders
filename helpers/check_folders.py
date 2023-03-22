import os


class Helper():
    def check_folders_existents(self, folder: str) -> bool:
        check = os.path.isdir(folder)
        if not check:
            return True
        return False

    def create_languages_folders(self) -> list:
        files_name = os.listdir("files/")
        files_name = [name.split('-')[0] for name in files_name if name.endswith('.txt')]
        unique_folders_name = list(set(files_name))
        for folder in unique_folders_name:
            result = self.check_folders_existents(f"files/{folder}")
            if result:
                os.mkdir(f"files/{folder}")

        return unique_folders_name
