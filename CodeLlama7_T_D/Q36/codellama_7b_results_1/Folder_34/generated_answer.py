
def filter_chars(string):
    # create a list of characters in the given string
    char_list = list(string)

    # loop through each character in the list
    for i, char in enumerate(char_list):
        # check if the character is between the indices 10 and 79 (both exclusive)
        if 10 < i < 79:
            # check if the character is greater than '?' and smaller than 'm'
            if ord('?') < ord(char) < ord('m'):
                # remove all occurrences of that character in the string
                char_list = [c for c in char_list if c != char]

    # return the altered string
    return ''.join(char_list)
