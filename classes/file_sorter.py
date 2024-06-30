import os

class FileSorter:
    def __init__(self, directory):
        self.directory = directory

    def sort_by_name(self):
        files = sorted(os.listdir(self.directory))
        return files

    def sort_by_size(self):
        files = sorted(os.listdir(self.directory), key=lambda f: os.path.getsize(os.path.join(self.directory, f)))
        return files

    def sort_by_modification_date(self):
        files = sorted(os.listdir(self.directory), key=lambda f: os.path.getmtime(os.path.join(self.directory, f)))
        return files

    def sort_by_creation_date(self):
        files = sorted(os.listdir(self.directory), key=lambda f: os.path.getctime(os.path.join(self.directory, f)))
        return files

    # Add more sorting methods based on other attributes as needed
