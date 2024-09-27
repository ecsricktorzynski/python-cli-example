import os

def list_files(path):
    
    files = os.listdir(path)

    # Filter out non-files if needed (like directories)
    files = [f for f in files if os.path.isfile(os.path.join(path, f))]

    # Sort files
    files.sort()

    return files

if __name__ == '__main__':
    files = []
    dir_path = '/home/rick/github/python-cli-example'

    files = list_files(dir_path)
    
    print(f"Files in {dir_path}:\n")
    for file in files:
        print(f"{file}")
