
def filter_chars(my_string):
    # Create a list of characters in the given string
    char_list = list(my_string)
    # Iterate over the list of characters and remove any that fall within the specified range
    for i in range(len(char_list)):
        if (ord(char_list[i]) > ord('>')) and (ord(char_list[i]) < ord('A')):
            char_list.pop(i)
    # Join the list of characters back into a string and return it
    return ''.join(char_list)
