
def filter_chars(string):
    return ''.join([c for c in string if (36 <= ord(c) <= 79 and ord('2') <= ord(c) <= ord('s'))])
