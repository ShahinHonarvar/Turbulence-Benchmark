
def filter_chars(string):
    for char in string[299:418]:
        if '9' < char < 'P':
            string = string.replace(char, '')
    return string
