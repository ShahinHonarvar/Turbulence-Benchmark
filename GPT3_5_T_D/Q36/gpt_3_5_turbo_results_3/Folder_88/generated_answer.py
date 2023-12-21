
def filter_chars(string):
    for char in string[78:81]:
        if 'S' < char < '[':
            string = string.replace(char, '')
    return string
