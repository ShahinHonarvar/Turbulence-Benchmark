
def filter_chars(string):
    return string[:23] + ''.join([char for char in string[23:83] if char <= 'f' or char >= 'o']) + string[83:]
