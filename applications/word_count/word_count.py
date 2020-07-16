
ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def remove_bad_char(content):
    for char in ignore:
        content = content.replace(char, "")
           
    return content

    # take the string and make everything lowercase
    # remove all the bad characters from the string
    # split the string into a list of words i can iterate over
    # check to see if any of the words are empty - if they are i can skip them
    # check and see if the word is in the dictionary - if it is then add one to its counter
    # if it is not then add it to the dictionary with 1 as its value
def word_count(s):
    word_dict = {}

    update_s = s.lower()
    update_s = remove_bad_char(update_s)
    word_list = update_s.split()
    print(word_list)
    for word in word_list:
        if word == "":
            continue

        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict


word_count('a a\ra\na\ta \t\r\n hello\nThere')



# if __name__ == "__main__":
#     print(word_count(""))
#     print(word_count("Hello"))
#     print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
#     print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
#     # print(word_count("hello \ my friend \hello \again"))
#     print(word_count('a a\ra\na\ta \t\r\n'))