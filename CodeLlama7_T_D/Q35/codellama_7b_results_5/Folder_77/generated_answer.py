
def remove_repeat_chars(string):
    # Create a new string with the characters from the original string, but without any repeated characters
    new_string = ""
    for i in range(len(string)):
        if string[i] not in new_string:
            new_string += string[i]
    return new_string
