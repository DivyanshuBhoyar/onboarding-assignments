def test_create_temp_file(tmp_path):
    temp_file = tmp_path / "temp.txt"
    temp_file.write_text("Hello, pytest!")
    assert temp_file.read_text() == "Hello, pytest!"