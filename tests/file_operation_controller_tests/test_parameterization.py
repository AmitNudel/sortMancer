import shutil
import pytest

from unittest.mock import patch
from classes.file_operation_controller import FileOperationController

@pytest.mark.parametrize("src, dest", [
    ("file1.txt", "file2.txt"),
    ("testfile1.txt", "testfile2.txt"),
    ("datafile1.txt", "datafile2.txt")
])
def test_parameterized_file_operations(tmp_path, src, dest):
    src_file = tmp_path / src
    src_file.write_text("Some content")
    dest_file = tmp_path / dest
    controller = FileOperationController(str(src_file), str(dest_file))

    with patch.object(shutil, 'move', return_value=None) as mock_move:
        controller.move_file()
        mock_move.assert_called_once_with(str(src_file), str(dest_file))
