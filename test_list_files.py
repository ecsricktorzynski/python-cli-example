# test_list_files.py

import os
import pytest
from assignment import list_files  # Replace with the actual name of the module where list_files is defined

def test_list_files(tmp_path):
    # Create some sample files in the temporary directory
    file1 = tmp_path / "b.txt"
    file2 = tmp_path / "a.txt"
    file3 = tmp_path / "c.txt"
    
    # Touch the files to create them
    file1.touch()
    file2.touch()
    file3.touch()
    
    # Get the list of files from the directory
    expected_files = ['a.txt', 'b.txt', 'c.txt']
    result = list_files(tmp_path)
    
    # Check if the files are listed and sorted correctly
    assert result == expected_files
