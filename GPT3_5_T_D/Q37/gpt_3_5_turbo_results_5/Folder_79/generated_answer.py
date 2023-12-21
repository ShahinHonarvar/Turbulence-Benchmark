
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 10 or i > 52 or not ('@' <= char <= 'T'))
