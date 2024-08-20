student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#Creating a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row['letter']:row['code'] for (index, row) in df.iterrows()}

#Creating a list of the phonetic code words from a word that the user inputs.
answer = input("What is the word?: ")
code_list = [nato_alphabet_dict.get(letter.upper()) for letter in answer if letter.upper() in nato_alphabet_dict]
print(code_list)