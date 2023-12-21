
def remove_repeat_chars(string):
    for char in string:
        if 0 < string.index(char) < 10 and string.count(char) > 1:
            string = string.replace(char, '')
    return string
