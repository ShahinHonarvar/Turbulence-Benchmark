
def filter_chars(string):
    return string[:38] + ''.join([char for char in string[38:81] if char <= '.' or char >= '^']) + string[81:]
