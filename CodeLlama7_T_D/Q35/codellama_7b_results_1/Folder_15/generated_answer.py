
def remove_repeat_chars(s):
    # create a new string with the characters removed
    new_str = ''
    # loop through each character in the original string
    for char in s:
        # if the current character is not already in the new string
        if char not in new_str:
            # add the current character to the new string
            new_str += char

    # return the altered string
    return new_str
