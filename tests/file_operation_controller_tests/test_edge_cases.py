import shutil

from unittest.mock import MagicMock, patch
from classes.file_operation_controller import ErrorHandler, FileOperationController

def test_move_empty_file(tmp_path):
    empty_file = tmp_path / "empty_file.txt"
    empty_file.touch()  # Create an empty file
    dest_file = tmp_path / "moved_empty_file.txt"
    controller = FileOperationController(str(empty_file), str(dest_file))

    with patch.object(shutil, 'move', return_value=None) as mock_move:
        controller.move_file()
        mock_move.assert_called_once_with(str(empty_file), str(dest_file))

def test_handle_special_characters(tmp_path):
    special_file = tmp_path / "spécial_fïle.txt"
    special_file.write_text("Some content")
    dest_file = tmp_path / "new_spécial_fïle.txt"
    controller = FileOperationController(str(special_file), str(dest_file))

    with patch.object(shutil, 'move', return_value=None) as mock_move:
        controller.move_file()
        mock_move.assert_called_once_with(str(special_file), str(dest_file))

def test_handle_disk_full_error():
    mock_action = MagicMock(side_effect=OSError("No space left on device"))
    mock_action.__name__ = 'move'
    with patch('builtins.print') as mock_print:
        ErrorHandler.handle_error(mock_action, "file_with_error")
        mock_print.assert_called_once_with("Error during move: No space left on device")

def test_handle_read_only_filesystem():
    mock_action = MagicMock(side_effect=OSError("Read-only file system"))
    mock_action.__name__ = 'copy2'
    with patch('builtins.print') as mock_print:
        ErrorHandler.handle_error(mock_action, "file_with_error")
        mock_print.assert_called_once_with("Error during copy2: Read-only file system")

