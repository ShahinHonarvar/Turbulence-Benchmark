
def remove_repeat_chars(string):
    # create a list of characters in the string
    char_list = list(string)

    # iterate through each character in the string

    for i, char in enumerate(char_list):
        # check if the current character occurs more than once between indices 80 and 200

        if char_list.count(char) > 1 and (i < 80 or i > 200):
            # remove all occurrences of the current character from the string

            while char in char_list:
                char_list.remove(char)

    return "".join(char_list)
