
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (373 <= i <= 901 and 'T' <= c <= 'h'))
