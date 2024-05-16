# with open("my_file.txt") as file: # don't have to remember to close file
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="w") as file:  # making it editable; w
#     file.write("New text.")

# with open("my_file.txt", mode="a") as file:  # making it editable; a appends
#     file.write("\nNew text.")

with open("new_file.txt", mode="w") as file:  # creates new file since there is no file named new_file.txt
    file.write("\nNew text.")