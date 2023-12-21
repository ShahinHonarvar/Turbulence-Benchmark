
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 27 or i > 29 or not (';' <= char <= 'b'))
