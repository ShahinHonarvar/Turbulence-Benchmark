
def remove_repeat_chars(string):
    new_string = ""

    for i, char in enumerate(string):
        if i > 10 and i < 76 and char in string[10:76] and string.count(char) > 1:
            continue
        new_string += char

    return new_string
