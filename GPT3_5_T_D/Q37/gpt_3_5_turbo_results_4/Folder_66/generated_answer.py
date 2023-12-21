
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if not (27 <= i <= 85) or char < 'c' or char > 'i')
