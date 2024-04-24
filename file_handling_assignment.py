# File Creation
try:
    # Open file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write three lines of text
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("This is line 3.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File creation completed.")

# File Reading and Display
try:
    # Open file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display contents
        print("Contents of my_file.txt:")
        print(file.read())
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File reading completed.")

# File Appending
try:
    # Open file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three lines of text
        file.write("This is line 4.\n")
        file.write("Appended line 5.\n")
        file.write("Another appended line, 6.\n")
except (FileNotFoundError, PermissionError) as e:
    print(f"Error: {e}")
finally:
    print("File appending completed.")
