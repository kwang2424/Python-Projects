# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

import pandas

# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}


nato_alpha = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}

# while True:
#     try:
#         user = input("Enter a word: ")
#         nato_word = [alphabet[letter.upper()] for letter in user]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         break


def generate_nato():
    user = input("Enter a word: ")
    try:
        nato_word = [alphabet[letter.upper()] for letter in user]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato()
    else:
        print(nato_word)


generate_nato()
