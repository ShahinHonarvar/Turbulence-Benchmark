
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 86 or i > 92 or not '!' <= char <= 's'])
