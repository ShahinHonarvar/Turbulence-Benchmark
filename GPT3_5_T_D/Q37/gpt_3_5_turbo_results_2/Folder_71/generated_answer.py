
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if (32 <= i <= 46) and ('0' <= char <= 'k'))
