
def filter_chars(string):
    return string[:63] + ''.join([char for char in string[63:89] if '*' >= char or char >= 'w']) + string[89:]
