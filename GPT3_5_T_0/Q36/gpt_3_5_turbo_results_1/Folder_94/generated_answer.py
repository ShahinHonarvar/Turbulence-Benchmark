
def filter_chars(string):
    return string[:15] + ''.join([char for char in string[15:85] if char <= 'I' or char >= 'M']) + string[85:]
