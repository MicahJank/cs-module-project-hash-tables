
ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def remove_bad_char(content):
    for char in content:
        # print(char)
        if char in ignore:
            content = content.replace(char, "")
           
    return content

    # take the string and split it using the split method - this will give me a list of the words
    # loop over the list of words and iterate over the individual strings to remove any unwanted characters
    # lowercase the word
    # check if the word is already in the cache of words - if its increase the count by 1 - if it is not add it to the cache and initialize it to 1
    # after that return the cache of words
def word_count(s):
    word_dict = {}
    # if check_ignored_char(s) == False:
    #     return {}
    s = remove_bad_char(s)
    word_list = s.split(" ")
    # print("word list", word_list)
    for word in word_list:
        # word = remove_bad_char(word)
        if word == "":
            continue

        word = word.lower()
        
        
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict





if __name__ == "__main__":
    # print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    # print(word_count("hello \ my friend \hello \again"))
    print(word_count('a a\ra\na\ta \t\r\n'))