import shutil
from pathlib import Path

source = Path("original.txt")
backup = Path("backup.txt")
copy_folder = Path("copies")

# Create source file
with open(source, "w", encoding="utf-8") as file:
    file.write("This is the original file.\n")

# Create directory for copied file
copy_folder.mkdir(exist_ok=True)

# Copy file
shutil.copy(source, backup)
print("File copied to backup.txt")

shutil.copy(source, copy_folder / "original_copy.txt")
print("File copied to copies/original_copy.txt")

# Safe delete
if backup.exists():
    backup.unlink()
    print("backup.txt deleted safely.")
else:
    print("backup.txt does not exist.")