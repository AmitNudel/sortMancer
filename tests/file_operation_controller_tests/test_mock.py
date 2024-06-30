from unittest.mock import MagicMock, patch
from classes.file_operation_controller import ErrorHandler


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
