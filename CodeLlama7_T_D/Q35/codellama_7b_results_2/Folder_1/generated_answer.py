 def remove_repeat_chars(string):
    # Create a new string with the characters from the original string that are not repeated between indices 17 and 88, both exclusive.
    new_string = ""
    for i in range(len(string)):
        if i < 17 or i > 88:
            new_string += string[i]
    return new_string
