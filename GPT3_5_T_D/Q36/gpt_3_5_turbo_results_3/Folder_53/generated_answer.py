
def filter_chars(string):
    return ''.join([c for c in string if not (90 < ord(c) < 97 and 'j' < c < 'w')])
