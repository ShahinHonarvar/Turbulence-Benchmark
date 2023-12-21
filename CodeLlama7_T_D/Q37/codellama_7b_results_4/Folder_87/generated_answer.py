
def filter_chars(s):
    # create a list of characters in the given string
    char_list = list(s)

    # iterate over each character in the list
    for i in range(len(char_list)):
        # check if the current character is between indices 18 and 81, both inclusive
        if (i >= 18 and i <= 81) and (char_list[i] >= 'W' and char_list[i] <= '['):
            # remove all occurrences of the current character from the list
            while char_list.count(char_list[i]) > 0:
                char_list.remove(char_list[i])

    # return the altered string
    return "".join(char_list)
