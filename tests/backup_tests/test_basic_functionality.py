import os
import shutil
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from classes.backup import BackupManager

@pytest.fixture
def setup_files(tmp_path):
    src_dir = tmp_path / "src_dir"
    src_dir.mkdir()
    src_file = src_dir / "src_file.txt"
    src_file.write_text("This is a test file.")
    backup_dir = tmp_path / "backup_dir"
    return src_dir, src_file, backup_dir

def test_backup_manager_init(setup_files):
    src_dir, _, backup_dir = setup_files
    manager = BackupManager(src_dir, backup_dir)
    assert manager.src == src_dir
    assert manager.backup_dir == backup_dir

def test_create_backup_folder_name(setup_files):
    src_dir, src_file, backup_dir = setup_files
    manager = BackupManager(src_dir, backup_dir)
    manager._create_backup_folder_name()
    assert os.path.exists(manager.backup_path)
    assert os.path.isdir(manager.backup_path)

def test_create_backup_for_file(setup_files):
    _, src_file, backup_dir = setup_files

    manager = BackupManager(src_file, backup_dir)

    with patch.object(shutil, 'copy2', return_value=None) as mock_copy:
        backup_path = manager.create_backup()

        assert os.path.exists(backup_path)
        assert mock_copy.called

# def test_create_backup_for_directory(setup_files):
#     src_dir, src_file, backup_dir = setup_files
#     manager = BackupManager(src_dir, backup_dir)
#     with patch.object(shutil, 'copy2', return_value=None) as mock_copy:
#         backup_path = manager.create_backup()
#         assert os.path.exists(backup_path)
#         mock_copy.assert_called_once_with(str(manager.src), str(backup_dir))
# need to check to pathing + naming 