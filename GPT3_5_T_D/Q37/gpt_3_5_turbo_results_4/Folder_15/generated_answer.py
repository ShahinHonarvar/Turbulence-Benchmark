
def filter_chars(string):
    return string[:2] + ''.join(c for c in string[2:7] if c < '?' or c > 'f') + string[7:]
