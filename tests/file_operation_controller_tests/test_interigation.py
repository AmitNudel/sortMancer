from classes.file_operation_controller import FileOperationController


def test_integration_file_operations(tmp_path):
    src_file = tmp_path / "integration_file.txt"
    src_file.write_text("Integration test content")
    dest_file = tmp_path / "moved_integration_file.txt"
    controller = FileOperationController(str(src_file), str(dest_file))

    # Test move operation
    controller.move_file()
    assert not src_file.exists()
    assert dest_file.exists()

    # Test copy operation
    controller = FileOperationController(str(dest_file), str(src_file))
    controller.copy_file()
    assert src_file.exists()
    assert dest_file.exists()

    # Test delete operation
    controller = FileOperationController(str(src_file))
    controller.delete_file()
    assert not src_file.exists()
    assert dest_file.exists()
