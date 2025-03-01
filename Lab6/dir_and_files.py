
#Ex1
import os

def list_directories_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll Directories and Files:")
    for item in os.listdir(path):
        print(item)

path = "."  # Current directory
list_directories_files(path)


#Ex2
import os

def check_path_access(path):
    print(f"Existence: {os.path.exists(path)}")
    print(f"Readability: {os.access(path, os.R_OK)}")
    print(f"Writability: {os.access(path, os.W_OK)}")
    print(f"Executability: {os.access(path, os.X_OK)}")

path = "example.txt"
check_path_access(path)


#Ex3
import os

def check_path_and_get_details(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print(f"The path '{path}' does not exist.")

path = "example.txt"
check_path_and_get_details(path)

#Ex4
def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        return len(file.readlines())

file_path = "example.txt"
line_count = count_lines_in_file(file_path)
print(f"Number of lines in '{file_path}': {line_count}")


#Ex5
def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(f"{item}\n")

file_path = "output.txt"
data = ["Apple", "Banana", "Cherry"]
write_list_to_file(file_path, data)
print(f"List written to '{file_path}'.")

#Ex6
import string
def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.txt")


generate_text_files()
print("26 text files generated.")

#Ex7
def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source, open(destination_path, 'w') as destination:
        destination.write(source.read())

source_path = "source.txt"
destination_path = "destination.txt"
copy_file(source_path, destination_path)
print(f"Contents of '{source_path}' copied to '{destination_path}'.")

import os
#Ex 8
def delete_file_if_accessible(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' deleted.")
        else:
            print(f"No write access to '{path}'. Cannot delete.")
    else:
        print(f"File '{path}' does not exist.")

path = "example.txt"
delete_file_if_accessible(path)