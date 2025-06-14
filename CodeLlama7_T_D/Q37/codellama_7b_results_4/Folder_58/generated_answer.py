
def filter_chars(s):
    # create a list of all characters in the string
    char_list = list(s)

    # iterate through the list and remove any characters that are outside the desired range
    for i, c in enumerate(char_list):
        if ord(c) < 9 or ord(c) > 119:
            char_list.pop(i)

    # join the filtered list of characters back into a string and return it
    return "".join(char_list)
