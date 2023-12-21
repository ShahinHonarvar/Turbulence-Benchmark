
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 37 or i > 56 or char < '6' or char > '_')
