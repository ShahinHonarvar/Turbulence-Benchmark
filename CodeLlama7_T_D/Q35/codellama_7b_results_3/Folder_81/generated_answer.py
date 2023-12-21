
def remove_repeat_chars(s):
    # create an empty list to store the characters
    char_list = []
    # iterate over each character in the input string
    for c in s:
        # if the current character is not already in the list
        if c not in char_list:
            # append the character to the list
            char_list.append(c)
    # create an empty string to store the output
    output = ""

    # iterate over each character in the input string
    for c in s:
        # if the current character is not already in the list
        if c not in char_list:
            # append the character to the list
            output += c

    # return the altered string
    return output
