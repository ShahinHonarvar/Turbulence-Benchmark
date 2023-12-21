
def filter_chars(string):
    return string[:31] + ''.join([c for c in string[31:73] if c <= 'M' or c >= 'j']) + string[73:]
