
def filter_chars(string):
    return ''.join([char for char in string if char <= '&' or char >= 'c' or char < 'C' or char > 'z'])
