
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 82 or i >= 93 or c <= '!' or c >= '*'])
