
def remove_repeat_chars(string):
    for char in string[34:69]:
        if string[34:69].count(char) > 1:
            string = string.replace(char, '')
    return string
