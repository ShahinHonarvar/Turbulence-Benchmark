
def remove_repeat_chars(string):
    if len(string) < 203:
        return string
    
    for char in set(string[200:202]):
        string = string.replace(char, '')

    return string
