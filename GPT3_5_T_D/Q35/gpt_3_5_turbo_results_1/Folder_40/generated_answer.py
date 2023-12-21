
def remove_repeat_chars(string):
    for char in set(string[:3]):
        string = string.replace(char, '')
    return string
