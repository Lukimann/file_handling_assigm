# File Creation
with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("12345\n")
    file.write("Another line with text and numbers\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading process complete.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("67890\n")
        file.write("Appending another line with text and numbers\n")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File appending process complete.")