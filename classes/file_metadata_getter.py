import os
import stat
import hashlib
import mimetypes
import datetime

class FileMetadataReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_file_size(self):
        return os.path.getsize(self.file_path)

    def get_file_creation_time(self):
        return datetime.datetime.fromtimestamp(os.path.getctime(self.file_path))

    def get_file_modification_time(self):
        return datetime.datetime.fromtimestamp(os.path.getmtime(self.file_path))

    def get_file_type(self):
        return mimetypes.guess_type(self.file_path)[0]

    def get_file_permissions(self):
        mode = os.stat(self.file_path).st_mode
        return stat.filemode(mode)

    def get_file_owner(self):
        return os.stat(self.file_path).st_uid

    def get_file_group(self):
        return os.stat(self.file_path).st_gid

    def get_file_checksum(self):
        with open(self.file_path, "rb") as f:
            file_hash = hashlib.sha256()
            while chunk := f.read(4096):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    
    # Additional methods for extracting specific metadata could be added here
