
def filter_chars(my_string):
    # create a list of characters between indices 54 and 92 (exclusive)
    char_list = my_string[54:92]
    # iterate over the list of characters and remove any character that is greater than 'J' and smaller than 'X'
    for i in range(len(char_list)):
        if char_list[i] > 'J' and char_list[i] < 'X':
            char_list.remove(char_list[i])
    # return the altered string
    return "".join(char_list)
