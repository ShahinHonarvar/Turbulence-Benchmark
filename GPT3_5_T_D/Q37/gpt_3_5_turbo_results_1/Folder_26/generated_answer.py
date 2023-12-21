
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 20 or i > 62 or char < 'i' or char > 'k')
