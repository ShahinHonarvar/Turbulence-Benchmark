
def filter_chars(s):
    return ''.join(c for i, c in enumerate(s) if i < 503 or i > 753 or c < '9' or c > 'w')
