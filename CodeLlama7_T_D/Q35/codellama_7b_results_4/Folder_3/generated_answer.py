
def remove_repeat_chars(string):
    # Create a new string with the characters from the original string
    # that do not occur more than once between indices 56 and 88, both exclusive
    new_string = ""

    for i in range(len(string)):
        if (i < 56 or i > 88) and string.count(string[i]) == 1:
            new_string += string[i]

    return new_string
