
def remove_repeat_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if 10 < i < 76 and char in string[10:i]:
            continue
        new_string += char
    return new_string
