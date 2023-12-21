
def filter_chars(string):
    for char in string[79:81]:
        if 'S' < char < '[':
            string = string.replace(char, '')
    return string
