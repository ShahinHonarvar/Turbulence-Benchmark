
def filter_chars(string):
    return ''.join(char for char in string if char not in set(string[29:98]) and '-' <= char <= 'n')
