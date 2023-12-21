
def filter_chars(s):
    # create a list of all characters in the string
    char_list = list(s)

    # iterate through the characters between indices 27 and 29, inclusive
    for i in range(27, 30):
        # if the character is greater than or equal to ';' and smaller than or equal to 'b', remove all occurrences of that character from the string
        if char_list[i] >= ';' and char_list[i] <= 'b':
            while char_list[i] in char_list:
                # remove the character from the list
                char_list.remove(char_list[i])
    # join the remaining characters in the list into a single string
    altered_string = "".join(char_list)
    return altered_string
