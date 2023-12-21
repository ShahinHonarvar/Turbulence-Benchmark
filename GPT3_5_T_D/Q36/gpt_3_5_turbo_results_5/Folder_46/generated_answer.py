
def filter_chars(string):
    return string[:19] + string[69:] + ''.join([ch for ch in string[19:69] if ch <= '<' or ch >= 'C'])
