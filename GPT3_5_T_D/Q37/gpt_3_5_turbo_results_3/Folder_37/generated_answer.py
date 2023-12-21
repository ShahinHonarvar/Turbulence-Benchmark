
def filter_chars(string):
    return ''.join(char for char in string if char < 'O' or char > '^' or char not in string[17:64])
