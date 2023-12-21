
def remove_repeat_chars(string):
    for index, char in enumerate(string[200:202]):
        if string.count(char) > 1:
            string = string.replace(char, '')
    return string
