import sys
import os

# Recursively get folders in the current directory


def get_files_in_folder(path):
    files = []
    if ("node_modules" in path) or (".git" in path):
        return files

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if "." not in file:
                continue
            files.append(os.path.join(path, file))
        else:
            files.extend(get_files_in_folder(os.path.join(path, file)))
    return files


# Get line count of a file
def get_line_count(file):
    with open(file, "r") as f:
        try:
            return len(f.readlines())
        except UnicodeDecodeError:
            return 0


if len(sys.argv) == 1:
    print("Directory argument is required")
    sys.exit(1)

directory = sys.argv[1]
path = os.path.join(directory)

if not os.path.exists(path):
    print("Directory does not exist")
    sys.exit(1)

total_lines = 0

files = get_files_in_folder(path)
for file in files:
    file_lines = get_line_count(file)
    print(file + ": " + str(file_lines))
    total_lines += file_lines

print()
print("TOTAL LINES:", total_lines)
