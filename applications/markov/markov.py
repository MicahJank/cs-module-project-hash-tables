import random

words_list = None
data_set = {}
# Read in all the words in one go
with open("./markov/input.txt") as f:
    words = f.read()
    words_list = words.split(" ")

# TODO: analyze which words can follow other words
'''
iterate over the words list
for each word i will need to check and see if the word exists in the data set yet or not
if it does exist in the data set i need to take the next word in the list and add it to the array at the position in the data set
if it does not exist in the data set i need to create that word in the data set and add the next word in the list to the array associate with the newly created key
'''
# this is the function that creates the crazy sentence
def create_nonsense(word):
    current_word = word
    print(current_word, end=" ")

    punctuation = [".", "!", "?"]
    running = True
    # check if we should stop
    while running is True:
        if current_word[-1] == '"':
            
        if current_word[-1] in punctuation:
            
    # otherwise randomly choose another word

for i, word in enumerate(words_list):
    # at the end of the list there cannot be any words that follow, so in that case i should just skip
    if i == (len(words_list) - 1):
        continue
    else:
        next_word = words_list[i+1]
        if word in data_set:
            data_set[word].append(next_word)
        else:
            data_set[word] = [next_word]


start_word = random.choice(words_list)

create_nonsense(start_word)


# TODO: construct 5 random sentences
# Your code here

