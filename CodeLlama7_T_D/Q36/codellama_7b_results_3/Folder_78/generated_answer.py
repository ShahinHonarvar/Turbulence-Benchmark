
def filter_chars(string):
    # Create a new string with all characters removed
    # that are between the indices 29 and 33 (both exclusive)
    new_string = ""
    for i in range(len(string)):
        if i < 29 or i > 33:
            new_string += string[i]
    return new_string
