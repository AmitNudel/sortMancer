import os
from datetime import datetime

class BackupManager:
    def __init__(self, src, backup_dir):
        self.src = src
        self.backup_dir = backup_dir
        self._validate_backup_dir()

    def _validate_backup_dir(self):
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
        elif not os.path.isdir(self.backup_dir):
            raise ValueError("Backup path must be a directory")

    def _create_backup_folder_name(self):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_folder_name = f"{os.path.basename(self.src)}_backup_{timestamp}"
        self.backup_path = os.path.join(self.backup_dir, backup_folder_name)
        os.makedirs(self.backup_path, exist_ok=True)
    
    def _backup_file(self, file_path):
        dest_path = os.path.join(self.backup_path, os.path.basename(file_path))
        file_controller = FileOperationController(file_path, dest_path)
        file_controller.copy_file()

    def create_backup(self):
        self._create_backup_folder_name()
        if os.path.isdir(self.src):
            for root, _, files in os.walk(self.src):
                for file in files:
                    file_path = os.path.join(root, file)
                    self._backup_file(file_path)
        else:
            self._backup_file(self.src)
        
        return self.backup_path
