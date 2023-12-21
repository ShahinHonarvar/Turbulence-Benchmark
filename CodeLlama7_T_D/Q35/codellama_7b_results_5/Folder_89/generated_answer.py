
def remove_repeat_chars(string):
    # create a list of characters in the given string
    char_list = list(string)

    # loop through each character in the list and check if it occurs more than once between indices 55 and 84, both exclusive
    for i in range(len(char_list)):
        if char_list[i] in string[55:84]:
            # remove all occurrences of the current character from the string
            char_list = [char for char in char_list if char != char_list[i]]

    # join the list of characters back into a string and return it
    return "".join(char_list)
