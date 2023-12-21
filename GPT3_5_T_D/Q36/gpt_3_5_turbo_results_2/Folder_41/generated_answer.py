
def filter_chars(string):
    return string[:81] + ''.join([char for char in string[81:89] if char <= 'f' or char >= '{']) + string[89:]
