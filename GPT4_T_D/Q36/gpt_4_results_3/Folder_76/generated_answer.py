
def filter_chars(str):
    for char in str[670:888]:
        if 'B' < char < 'Y':
            str = str.replace(char, '')
    return str
