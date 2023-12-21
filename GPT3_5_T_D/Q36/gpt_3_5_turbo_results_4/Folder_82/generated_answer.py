
def filter_chars(string):
    return ''.join([char for char in string if char <= 'V' or char >= 'j' or string.index(char) < 69 or string.index(char) >= 97])
