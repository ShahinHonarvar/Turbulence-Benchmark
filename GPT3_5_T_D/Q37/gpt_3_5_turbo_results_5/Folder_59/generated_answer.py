
def filter_chars(string):
    return ''.join(char for i, char in enumerate(string) if i < 2 or i > 3 or not ('5' <= char <= '_'))
