
def filter_chars(string):
    return string[:52] + ''.join([char for char in string[52:88] if char <= '&' or char >= 'c']) + string[88:]
