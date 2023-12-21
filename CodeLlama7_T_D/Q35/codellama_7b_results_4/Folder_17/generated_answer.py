 def remove_repeat_chars(string):
    # create a list of all characters in the string
    char_list = list(string)
    # loop through each character in the list and check if it occurs more than once between indices 73 and 84, both exclusive
    for i in range(len(char_list)):
        char = char_list[i]
        if string.count(char) > 1:
            # get the indices of all occurrences of the character in the string
            indices = [j for j, ltr in enumerate(string) if ltr == char]
            # check if any of the indices are between 73 and 84, both exclusive
            if not any(i >= 73 and i < 84 for i in indices):
                # remove all occurrences of the character from the string
                string = ''.join([ltr for ltr in string if ltr != char])
    return string
