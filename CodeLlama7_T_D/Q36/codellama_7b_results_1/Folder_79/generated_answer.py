
def filter_chars(s):
    # create a list of characters in the given string
    char_list = list(s)
    # iterate over each character in the list
    for i, c in enumerate(char_list):
        # check if the current character is between 11 and 46 (exclusive)
        if 11 <= ord(c) < 46:
            # remove all occurrences of the current character from the string
            char_list = [x for x in char_list if x != c]
    # join the list of characters back into a string and return it
    return "".join(char_list)
