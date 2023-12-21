
def remove_repeat_chars(string):
    for char in set(string):
        if 70 < string.index(char) < 200:
            string = string.replace(char, '')
    return string
