
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 5 or i > 6 or char < 'G' or char > 'p')
