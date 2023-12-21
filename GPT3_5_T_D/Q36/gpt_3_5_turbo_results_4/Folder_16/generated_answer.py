
def filter_chars(s):
    return s[:331] + ''.join(c for c in s[331:713] if c <= 'M' or c >= '_') + s[713:]
