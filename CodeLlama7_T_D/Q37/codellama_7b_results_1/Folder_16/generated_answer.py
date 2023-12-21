
def filter_chars(string):
    # create a list of characters in the given string
    char_list = list(string)

    # iterate through each character in the list
    for i, char in enumerate(char_list):
        # check if the character is between indices 225 and 381, both inclusive
        if 225 <= i <= 381:
            # check if the character is greater than or equal to 'D' and smaller than or equal to 'Y'
            if char >= 'D' and char <= 'Y':
                # remove all occurrences of that character from the string
                string = string.replace(char, '')

    return string
