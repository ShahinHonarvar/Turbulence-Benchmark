
def filter_chars(string):
    return ''.join(char for idx, char in enumerate(string) if (46 <= idx <= 85) and ('-' <= char <= 'X'))
