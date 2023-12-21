
def filter_chars(str):
    for char in str[47:68]:
        if 'H' < char < 's':
            str = str.replace(char, '')
    return str
