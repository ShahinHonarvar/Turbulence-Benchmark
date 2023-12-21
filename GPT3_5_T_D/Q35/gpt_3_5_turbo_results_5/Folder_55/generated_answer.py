
def remove_repeat_chars(string):
    new_string = ''
    for index, char in enumerate(string):
        if index < 10 or index >= 100 or string.count(char) <= 1:
            new_string += char
    return new_string
