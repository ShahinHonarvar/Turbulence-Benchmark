 def filter_chars(s):
    # initialize a new string to store the filtered characters
    new_string = ""

    # loop through each character in the input string
    for char in s:

        # if the current character is within the specified range and meets the condition, do not include it in the output string
        if (char >= ':' and char <= 'r') and (char not in new_string):
            new_string += char

        # otherwise, include the character in the output string
        else:
            new_string += char

    # return the filtered string
    return new_string
