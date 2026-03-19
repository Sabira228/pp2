from pathlib import Path

# Create a sample file first so the example always works
file_path = Path("sample_read.txt")
file_path.write_text("First line\nSecond line\nThird line", encoding="utf-8")

# Read the whole file
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print("read():")
    print(content)

# Read one line
with open(file_path, "r", encoding="utf-8") as file:
    first_line = file.readline()
    print("\nreadline():")
    print(first_line)

# Read all lines into a list
with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("readlines():")
    print(lines)