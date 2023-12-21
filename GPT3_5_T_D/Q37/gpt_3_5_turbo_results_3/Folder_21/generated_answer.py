
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 603 or i > 759 or c < 'Q' or c > 'h')
