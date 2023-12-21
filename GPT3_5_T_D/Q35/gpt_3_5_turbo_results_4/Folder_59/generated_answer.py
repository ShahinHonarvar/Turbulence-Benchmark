
def remove_repeat_chars(string):
    if len(string) < 2:
        return string
    for char in string[1:10]:
        if string.count(char) > 1:
            string = string.replace(char, '')
    return string
