
def filter_chars(string):
    return ''.join(c for c in string if not (45 <= ord(c) < 57 and 'F' < c < 'n'))
