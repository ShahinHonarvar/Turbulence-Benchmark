 
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if (41 <= i <= 79) and ('f' <= c <= '|')])
