
def remove_repeat_chars(s):
    # create a list of characters in the given string
    char_list = list(s)
    # initialize an empty list to store the altered characters
    altered_chars = []
    # iterate through the characters in the given string
    for char in char_list:
        # if the current character is not already in the altered_chars list
        if char not in altered_chars:
            # add all occurrences of the current character to the altered_chars list
            while char in s:
                altered_chars.append(char)
    # create a new string from the altered characters list
    altered_string = "".join(altered_chars)
    # return the altered string
    return altered_string
