
def filter_chars(string):
    return ''.join([c for c in string if ord(c) < 72 or ord(c) > 93])
