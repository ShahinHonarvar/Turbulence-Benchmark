 def filter_chars(s):
    # create a list of characters in the given string
    char_list = list(s)
    # iterate through the list of characters
    for i in range(len(char_list)):
        # check if the current character is between indices 1 and 6 (both exclusive)
        if 1 < i < 6:
            # check if the current character is greater than ',' and smaller than 'f'
            if char_list[i] > ',' and char_list[i] < 'f':
                # remove all occurrences of the current character within the string while keeping the order of all characters intact
                char_list = char_list[:i] + char_list[i+1:]
    return "".join(char_list)
