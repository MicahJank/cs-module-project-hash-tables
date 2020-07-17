import random

words_list = None
data_set = {}
punctuation = [".", "!", "?"]

# Read in all the words in one go
with open("./markov/input.txt") as f:
    words = f.read()
    words_list = words.split(" ")
    f.close()

# TODO: analyze which words can follow other words
'''
iterate over the words list
for each word i will need to check and see if the word exists in the data set yet or not
if it does exist in the data set i need to take the next word in the list and add it to the array at the position in the data set
if it does not exist in the data set i need to create that word in the data set and add the next word in the list to the array associate with the newly created key
'''
# this is the function that creates the crazy sentence
# eg - "Pink brown bunnies!"
def create_nonsense(word):
    print(word, end=" ")    
    if word[-1] == '"' and word[-2] in punctuation:
        return word
    elif word[-1] in punctuation:
        return word
    
    # current_word = word
    next_word = random.choice(data_set[word])

    return word + " " + create_nonsense(next_word)

def choose_start_word():
    possibilities = random.choices(words_list, k=5)

    for word in possibilities:
        if word[0].isupper():
            return word
        elif word[0] == '"' and word[1].isupper():
            return word

    # if none of the 5 choices are what i want then i use recursion to re run the function until i get start word
    return choose_start_word()
        

def create_data_set():
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


create_data_set()
# make sure start word begins with a capital or " followed by a capital
start_word = choose_start_word()
nonsense = create_nonsense(start_word)


# # clear the output.txt before filling it out with the nonsense
with open('./markov/output.txt', "r+") as data:
    data.truncate(0)
    data.write(nonsense)
    data.close()

