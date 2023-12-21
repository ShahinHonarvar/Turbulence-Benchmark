
def remove_repeat_chars(string):
    for char in string:
        if string.count(char) > 1 and 33 < string.index(char) < 78:
            string = string.replace(char, '')
    return string
