 
def filter_chars(string):
    return ''.join([ch for ch in string if not(69 <= string.index(ch) <= 80 and '@' <= ch <= 'p')])
