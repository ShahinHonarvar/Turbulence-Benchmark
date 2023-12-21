
def filter_chars(string):
    return ''.join(char for idx, char in enumerate(string) if idx < 41 or idx > 79 or char < 'f' or char > '|')
