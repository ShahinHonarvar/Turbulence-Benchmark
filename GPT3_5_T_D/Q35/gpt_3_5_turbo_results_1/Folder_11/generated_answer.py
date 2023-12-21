
def remove_repeat_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if i < 48 or i >= 76 or string.count(char) == 1:
            new_string += char
    return new_string
