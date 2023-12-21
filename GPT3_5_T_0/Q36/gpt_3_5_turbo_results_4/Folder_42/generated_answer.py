
def filter_chars(string):
    return string[:42] + ''.join([char for char in string[42:68] if char <= 't' or char >= 'x']) + string[68:]
