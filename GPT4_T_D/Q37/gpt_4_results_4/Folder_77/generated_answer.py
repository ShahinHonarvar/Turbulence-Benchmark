
def filter_chars(s):
    removal_chars = [c for i, c in enumerate(s) if i >= 384 and i <= 411 and c >= '/' and c <= '8']
    for char in removal_chars:
        s = s.replace(char, '')
    return s
