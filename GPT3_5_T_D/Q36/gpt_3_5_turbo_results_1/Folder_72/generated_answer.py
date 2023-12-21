
def filter_chars(string):
    return string[:44] + ''.join([char for char in string[44:68] if char <= 'W' or char >= 'x']) + string[68:]
