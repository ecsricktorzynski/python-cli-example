# test_assignment.py

import os
import pytest
from click.testing import CliRunner
from assignment import cli_list_files

def test_list_files_cli_recursive(tmp_path):
    # Create a temporary directory and files for testing
    (tmp_path / "b.txt").touch()
    (tmp_path / "a.txt").touch()
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "c.txt").touch()

    # Initialize the Click testing runner
    runner = CliRunner()

    # Run the CLI tool with the path to the temporary directory and recursive option
    result = runner.invoke(cli_list_files, [str(tmp_path), '--recursive'])

    # Check if the output contains the sorted list of files
    expected_output = "a.txt\nb.txt\nsubdir/c.txt\n"
    assert result.exit_code == 0
    assert result.output == expected_output
