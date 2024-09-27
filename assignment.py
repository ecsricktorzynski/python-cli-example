import os
import click

# Define the function that lists and sorts files in a directory (with optional recursion)
def list_files(path, recursive=False):
    if recursive:
        # Use os.walk() to list files recursively
        files = []
        for root, dirs, filenames in os.walk(path):
            for file in filenames:
                files.append(os.path.relpath(os.path.join(root, file), path))
        files.sort()  # Sort the list of files
    else:
        # List files in the given directory only (non-recursive)
        files = os.listdir(path)
        files.sort()  # Sort the list of files

    return files

# Create a Click command to make the list_files function accessible from the CLI
@click.command()
@click.argument('path')  # Accept the directory path as an argument
@click.option('--recursive', is_flag=True, help="List files recursively.")  # Add a flag for recursive listing
def cli_list_files(path, recursive):
    """CLI tool that lists and sorts files in a directory, with optional recursion."""
    try:
        # Call the list_files function and print the result
        files = list_files(path, recursive)
        if files:
            for file in files:
                print(file)
        else:
            click.echo("No files found in the specified directory.")
    except FileNotFoundError:
        click.echo(f"Error: The directory '{path}' does not exist.")
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")

# Ensure the CLI command gets executed when the script is run
if __name__ == '__main__':
    cli_list_files()
