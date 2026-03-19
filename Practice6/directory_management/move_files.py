import shutil
from pathlib import Path

source_dir = Path("source_folder")
target_dir = Path("target_folder")

source_dir.mkdir(exist_ok=True)
target_dir.mkdir(exist_ok=True)

file_path = source_dir / "example.txt"

# Create file
with open(file_path, "w", encoding="utf-8") as file:
    file.write("This file will be moved and copied.\n")

# Copy file
shutil.copy(file_path, target_dir / "copied_example.txt")
print("File copied.")

# Move file
shutil.move(str(file_path), str(target_dir / "moved_example.txt"))
print("File moved.")

# Find files by extension
print("\nFiles with .txt extension in target_folder:")
for file in target_dir.glob("*.txt"):
    print(file.name)