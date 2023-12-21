
def remove_repeat_chars(s):
    # create an empty list to store the characters
    chars = []

    # loop through each character in the string
    for c in s:
        # if the current character is not already in the list
        if c not in chars:
            # add the character to the list
            chars.append(c)

    # create an empty string to store the altered string
    result = ""

    # loop through each character in the list
    for c in chars:
        # check if the current character is also in the original string
        if c in s:
            # add the character to the altered string
            result += c

    return result
