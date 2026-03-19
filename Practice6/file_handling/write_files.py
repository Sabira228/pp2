from pathlib import Path

file_path = Path("sample_write.txt")

# Write mode: creates or overwrites file
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("This is a file writing example.\n")

print("File created and written in 'w' mode.")

# Append mode: adds new content
with open(file_path, "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")

print("New line appended in 'a' mode.")

# Read back to verify
with open(file_path, "r", encoding="utf-8") as file:
    print("\nUpdated file content:")
    print(file.read())

# Exclusive creation mode: creates file only if it does not exist
new_file = Path("exclusive_file.txt")
if not new_file.exists():
    with open(new_file, "x", encoding="utf-8") as file:
        file.write("This file was created using x mode.\n")
    print("exclusive_file.txt created with 'x' mode.")
else:
    print("exclusive_file.txt already exists.")