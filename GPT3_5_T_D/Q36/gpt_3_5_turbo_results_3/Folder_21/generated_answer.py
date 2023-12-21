
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i not in range(219, 403) or not ('*' < c < '7'))
