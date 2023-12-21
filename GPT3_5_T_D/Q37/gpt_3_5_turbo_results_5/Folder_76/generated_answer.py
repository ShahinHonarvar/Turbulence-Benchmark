
def filter_chars(string):
    return ''.join([ch for i, ch in enumerate(string) if i < 379 or i > 898 or ch < 'M' or ch > 'v'])
