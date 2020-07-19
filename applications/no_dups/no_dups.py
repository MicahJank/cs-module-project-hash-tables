# i need to take the string and return the same string with the duplicate words removed
# only letters a-z are in the string
# no extra white space in the string allowed

def no_dups(s):
# duplicate_words can store the duplicate words in the string, this will help elimate duplicates because when adding a word to the string
# i can check and see if the word already exists and if it does i dont add it
    duplicate_words = {}
    # create a variable to store the de-dupped string
    # take s and split it by spaces
    # take the resulting list and iterate over it 
    # check to see if the word in the list is in the duplicate_words dict
    # if the word is in the dict then i can skip that word and dont add it to the string
    # if the word is not in the dictionary i can add it to the string variable and also add it to the dict
    # after i have all the words in the de-dupped string i can cut off excess space by using the .strip method on the string

    edited_str = ''
    words = s.split(" ")

    for word in words:
        if word not in duplicate_words:
            duplicate_words[word] = word
            edited_str += " " + word
    
    edited_str = edited_str.strip()

    return edited_str


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))