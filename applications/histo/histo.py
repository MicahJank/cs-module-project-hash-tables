words_list = []
ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
historgram = {}

def remove_bad_char(content):
    for char in ignore:
        content = content.replace(char, "")
           
    return content

words = open("./histo/robin.txt").read()

def create_histogram(words):
    words = words.lower()
    update_s = remove_bad_char(words)
    word_list = update_s.split()
    # print(word_list)
    for word in word_list:
        if word == "":
            continue

        if word in historgram:
            historgram[word] += '#'
        else:
            historgram[word] = '#'

    return historgram


create_histogram(words)

# make list from histogram to sort it 
histogram_list = list(historgram.items())
# lambda functions will sort first by the length(count) of hashtags want it in descending order so put the "-" in front
# secondary sorting will be done alphabetically in ascending order which is why we dont use any negatives there
sorted_list = sorted(histogram_list, key=lambda pair: (-len(pair[1]), pair[0]))

# i can use the length of the longest word to determine how much space we need to seperate the words from the hashes
longest_word = max(sorted_list, key=lambda  pair: len(pair[0]))
longest_word = longest_word[0]
print("longest_word", longest_word)
for pair in sorted_list:
    space = "  "
    # number_of_spaces = 2
    number_of_spaces =  len(longest_word) - len(pair[0])
    # print(number_of_spaces)
    space += " " * number_of_spaces
    # print(len(space))
    print(f"{pair[0]}{space}{pair[1]}")