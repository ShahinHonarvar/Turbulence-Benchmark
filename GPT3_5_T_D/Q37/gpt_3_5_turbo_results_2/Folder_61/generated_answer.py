
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if not(5 <= i <= 6 and 'G' <= char <= 'p'))
