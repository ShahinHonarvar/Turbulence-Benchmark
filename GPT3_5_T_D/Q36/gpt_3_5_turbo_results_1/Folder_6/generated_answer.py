
def filter_chars(string):
    return string[:31] + ''.join([c for c in string[31:70] if not ('B' < c < 'v')]) + string[70:]
