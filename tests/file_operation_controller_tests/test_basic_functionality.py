import os
import shutil
import pytest

from unittest.mock import patch, MagicMock
from classes.file_operation_controller import FileOperationController, ErrorHandler

@pytest.fixture
def setup_files(tmp_path):
    src_file = tmp_path / "src_file.txt"
    src_file.write_text("This is a test file.")
    dest_file = tmp_path / "dest_file.txt"
    return src_file, dest_file

def test_file_operation_controller_init():
    with pytest.raises(ValueError):
        FileOperationController(None)

    controller = FileOperationController("src_path")
    assert controller.src == "src_path"
    assert controller.dest is None

def test_move_file(setup_files):
    src_file, dest_file = setup_files
    controller = FileOperationController(str(src_file), str(dest_file))

    with patch.object(shutil, 'move', return_value=None) as mock_move:
        controller.move_file()
        mock_move.assert_called_once_with(str(src_file), str(dest_file))

def test_copy_file(setup_files):
    src_file, dest_file = setup_files
    controller = FileOperationController(str(src_file), str(dest_file))

    with patch.object(shutil, 'copy2', return_value=None) as mock_copy:
        controller.copy_file()
        mock_copy.assert_called_once_with(str(src_file), str(dest_file))

def test_delete_file(setup_files):
    src_file, _ = setup_files
    controller = FileOperationController(str(src_file))

    with patch('os.remove', return_value=None) as mock_remove:
        controller.delete_file()
        mock_remove.assert_called_once_with(str(src_file))

def test_rename_file(setup_files):
    src_file, dest_file = setup_files
    controller = FileOperationController(str(src_file), str(dest_file))

    with patch('os.rename', return_value=None) as mock_rename:
        controller.rename_file()
        mock_rename.assert_called_once_with(str(src_file), str(dest_file))

def test_handle_error_file_not_found():
    with patch('os.remove', side_effect=FileNotFoundError):
        with patch('builtins.print') as mock_print:
            ErrorHandler.handle_error(os.remove, "non_existent_file")
            mock_print.assert_called_once_with("Error: The source file non_existent_file does not exist.")

def test_handle_error_permission_denied():
    with patch('os.remove', side_effect=PermissionError):
        with patch('builtins.print') as mock_print:
            ErrorHandler.handle_error(os.remove, "protected_file")
            mock_print.assert_called_once_with("Error: Permission denied.")

def test_handle_error_general_exception():
    mock_action = MagicMock(side_effect=Exception("Unexpected error"))
    mock_action.__name__ = 'remove'
    with patch('builtins.print') as mock_print:
        ErrorHandler.handle_error(mock_action, "file_with_error")
        mock_print.assert_called_once_with("Error during remove: Unexpected error")

