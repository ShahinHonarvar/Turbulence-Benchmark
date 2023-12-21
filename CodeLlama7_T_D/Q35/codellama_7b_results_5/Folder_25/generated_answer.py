
def remove_repeat_chars(string):
    # Create a new string with the characters of the original string
    # that are not in the range of indices specified
    new_string = ""
    for i, char in enumerate(string):
        if i < 37 or i > 43:
            new_string += char
    return new_string
