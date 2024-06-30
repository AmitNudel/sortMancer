import shutil
from unittest.mock import patch
from classes.file_operation_controller import FileOperationController


def test_large_file_copy_performance(tmp_path):
    large_file = tmp_path / "large_file.txt"
    large_file.write_text("A" * 10**6)  # 1 MB file
    dest_file = tmp_path / "copied_large_file.txt"
    controller = FileOperationController(str(large_file), str(dest_file))

    import time
    start_time = time.time()
    with patch.object(shutil, 'copy2', return_value=None) as mock_copy:
        controller.copy_file()
        mock_copy.assert_called_once_with(str(large_file), str(dest_file))
    duration = time.time() - start_time
    assert duration < 1  # Ensure the operation is fast (less than 1 second)
