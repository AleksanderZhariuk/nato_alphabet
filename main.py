import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabet_data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_alphabet_data)
nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What's your name? ").upper()
result = [nato_alphabet[letter] for letter in user_input]
print(result)
