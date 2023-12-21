
def filter_chars(string):
    return ''.join(char for idx, char in enumerate(string) if idx < 51 or idx > 96 or char < 'X' or char > 'p')
