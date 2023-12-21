
def filter_chars(s):
    selected_chars = set([c for i, c in enumerate(s) if 603 <= i <= 759 and 'Q' <= c <= 'h'])
    return ''.join([c for c in s if c not in selected_chars])
