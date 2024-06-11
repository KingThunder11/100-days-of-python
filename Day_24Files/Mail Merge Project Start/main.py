#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]" # part of letter being replaced

# opens names list and reads it
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# opens starting letter and reads it. For loop takes each name, replaces the placeholder with the name,
# and makes a new letter and opens it in the correct file location
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip() # strips newline character
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
