
def filter_chars(string):
    # create a new string with the filtered characters
    new_string = ""

    # loop through each character in the original string
    for char in string:
        # if the current character is between indices 27 and 85, both inclusive, and is greater than or equal to character '!' and smaller than or equal to character 'B', then remove it from the new string
        if (27 <= ord(char) <= 85) and ('!' <= char <= 'B'):
            continue

        # otherwise, add the current character to the new string
        new_string += char

    # return the altered string
    return new_string
