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

# get the sum of the values in the count dict - this is useful for calculating each letters freq analysis
for char in cipher_text:
    if char == "W":
        cracked_text += "E"
    elif char == "J":
        cracked_text += "T"
    elif char == "M":
        cracked_text += "A"
    elif char == "X":
        cracked_text += "O"
    elif char == "C":
        cracked_text += "H"
    elif char == "D":
        cracked_text += "N"
    elif char == "K":
        cracked_text += "R"
    elif char == "I":
        cracked_text += "I"
    elif char == "N":
        cracked_text += "S"
    elif char == "U":
        cracked_text += "D"
    elif char == "S":
        cracked_text += "L"
    elif char == "O":
        cracked_text += "W"
    elif char == "G":
        cracked_text += "U"
    elif char == "Q":
        cracked_text += "G"
    elif char == "B":
        cracked_text += "F"
    elif char == "Y":
        cracked_text += "B"
    elif char == "E":
        cracked_text += "M"
    elif char == "F":
        cracked_text += "Y"
    elif char == "A":
        cracked_text += "C"
    elif char == "Z":
        cracked_text += "P"
    elif char == "P":
        cracked_text += "K"
    elif char == "H":
        cracked_text += "V"
    elif char == "V":
        cracked_text += "Q"
    elif char == "T":
        cracked_text += "J"
    elif char == "L":
        cracked_text += "X"
    elif char == "R":
        cracked_text += "Z"
    else:
        cracked_text += char
    


print(cracked_text)