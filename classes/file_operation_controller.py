import os
import shutil

class ErrorHandler:
    @staticmethod
    def handle_error(action, src, dest=None):
        try:
            if dest:
                action(src, dest)
            else:
                action(src)
        except FileNotFoundError:
            print(f"Error: The source file {src} does not exist.")
        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print(f"Error during {action.__name__}: {e}")
    

class FileOperationController:
    def __init__(self, src, dest=None):
        if not src:
            raise ValueError("Source path is required")
        self.src = src
        self.dest = dest

    def _perform_action(self, action):
        if not self.dest and action in {shutil.move, shutil.copy2, os.rename}:
            raise ValueError(f"Destination path is required for {action.__name__}")
        ErrorHandler.handle_error(action, self.src, self.dest)

    def move_file(self):
        self._perform_action(shutil.move)

    def copy_file(self):
        self._perform_action(shutil.copy2)

    def delete_file(self):
        self._perform_action(os.remove)

    def rename_file(self):
        self._perform_action(os.rename)