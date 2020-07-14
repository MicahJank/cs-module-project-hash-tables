# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

'''
- read the ciphertext.txt file and save its information so i can use it
- i will need a dictionairy to store the count of all occurrences for the letters in the cipher text
- i will also need a second dictionary that stores all letters and their respective frequency analysis (this is given to me in the readme)
- i need to intially loop over the text from the ciphertext file and store every occurrence of a letter in the count dictionary - i should ignore punctuation and non letter characters
- after that i need to loop again over the text again this time checking each letter with the count dictionary, i can then use that letters count to calculate the FA (number of occurences / total letters)
- i can then use the letters frequency analysis on the second dictionary to find what the true letter actually is
- i can then replace the letter with the true letter and move on to the next iteration
- i need to skip spaces
- i need to skip non letter characters
- everything is capitalized
- after everything i should save the new text into the cracked file
'''


cipher_text = ''
cracked_text = ''
with open("./crack_caesar/ciphertext.txt", "r") as data:
    cipher_text = data.read()

# print(cipher_text)

count_dict = {
    "E": 0,
    "T": 0,
    "A": 0,
    "O": 0,
    "H": 0,
    "N": 0,
    "R": 0,
    "I": 0,
    "S": 0,
    "D": 0,
    "L": 0,
    "W": 0,
    "U": 0,
    "G": 0,
    "F": 0,
    "B": 0,
    "M": 0,
    "Y": 0,
    "C": 0,
    "P": 0,
    "K": 0,
    "V": 0,
    "Q": 0,
    "J": 0,
    "X": 0,
    "Z": 0
}

caesar_key_dict = {}

FA_dict = {
    "E": 11.53,
    "T": 9.75,
    "A": 8.46,
    "O": 8.08,
    "H": 7.71,
    "N": 6.73,
    "R": 6.29,
    "I": 5.84,
    "S": 5.56,
    "D": 4.74,
    "L": 3.92,
    "W": 3.08,
    "U": 2.59,
    "G": 2.48,
    "F": 2.42,
    "B": 2.19,
    "M": 2.18,
    "Y": 2.02,
    "C": 1.58,
    "P": 1.08,
    "K": 0.84,
    "V": 0.59,
    "Q": 0.17,
    "J": 0.07,
    "X": 0.07,
    "Z": 0.03
}

# remove
# loop over the text to get the count of all letters in the count_dict
# remember to skip spaces and non letter characters
for char in cipher_text:
    # make sure i skip characters that dont need to be decoded
    if char.isalpha() == False or char == "â":
        continue
    else:
        count_dict[char] += 1


# loop through the count_dict and calculate the freq analysis for each number
for key, value in count_dict.items():
    freq_analysis = (value / sum(list(count_dict.values()))) * 100
    freq_analysis = round(freq_analysis, 2)

    # using the freq_analysis with the FA_dicts values i can compare to see which letters are paired with eachother
    for FA_key, FA_value in FA_dict.items():
        if FA_value == freq_analysis:
            caesar_key_dict[key] = FA_key

# print(caesar_key_dict)

# when trying to add the value from the dict to the cracked text - it will fail when the key is not in the dict
# in this case i can just add the char to the cracked text since the only cases where it will fail is when it is a space
# or some other non letter character that i dont have in the dict
for char in cipher_text:
    try:
        cracked_text += caesar_key_dict[char]
    except:
        cracked_text += char
    

# write the cracked code to the cracked.txt file
with open("./crack_caesar/cracked.txt", "w") as data:
    data.write(cracked_text)
    # cipher_text = data.read()

