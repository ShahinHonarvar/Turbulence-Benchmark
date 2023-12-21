
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 31 or i >= 73 or not ('M' < c < 'j'))
