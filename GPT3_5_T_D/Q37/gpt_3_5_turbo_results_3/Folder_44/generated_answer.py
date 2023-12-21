
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 21 or i > 43 or not ('+' <= c <= '8'))
