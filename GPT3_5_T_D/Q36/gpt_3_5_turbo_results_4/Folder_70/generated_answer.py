
def filter_chars(string):
    for char in string[170:195]:
        if '!' < char < '}':
            string = string.replace(char, '')
    return string
