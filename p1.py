file_path = "new_file.txt"
with open(file_path, 'w') as file:
    file.write("File Opening for pin Test")
    pin_name=input("enter a pin_name:")
print(f"File '{file_path}' created successfully.")
