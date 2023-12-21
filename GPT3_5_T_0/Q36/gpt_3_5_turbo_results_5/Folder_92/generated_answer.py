
def filter_chars(string):
    return string[0] + ''.join([char for char in string[1:6] if char <= ',' or char >= 'f']) + string[6:]
