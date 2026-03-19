import os
from pathlib import Path

# Current working directory
print("Current working directory:")
print(os.getcwd())

# Create one directory
os.mkdir("single_dir")
print("single_dir created.")

# Create nested directories
os.makedirs("parent_dir/child_dir/grandchild_dir", exist_ok=True)
print("Nested directories created.")

# List files and folders
print("\nContents of current directory:")
print(os.listdir())

# Change directory
os.chdir("single_dir")
print("\nChanged directory to:")
print(os.getcwd())

# Go back
os.chdir("..")
print("\nReturned to:")
print(os.getcwd())

# Remove empty directory
os.rmdir("single_dir")
print("single_dir removed.")

# pathlib example
path = Path("parent_dir")
print("\nPathlib exists():", path.exists())
print("Pathlib is_dir():", path.is_dir())