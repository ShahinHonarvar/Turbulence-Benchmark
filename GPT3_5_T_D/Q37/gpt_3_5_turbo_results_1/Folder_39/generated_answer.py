
def filter_chars(string):
    return ''.join(char for idx, char in enumerate(string) if idx < 52 or idx > 81 or char < 'A' or char > 'U')
