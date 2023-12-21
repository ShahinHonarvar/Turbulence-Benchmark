
def filter_chars(string):
    for char in string[3:8]:
        if '?' < char < 'k':
            string = string.replace(char, '')
    return string
