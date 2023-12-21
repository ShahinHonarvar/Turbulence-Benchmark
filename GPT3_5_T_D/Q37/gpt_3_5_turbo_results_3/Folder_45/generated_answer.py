
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 72 or i > 94 or char < '.' or char > 'b')
