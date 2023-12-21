
def filter_chars(s):
    to_filter = set(ch for i, ch in enumerate(s) if 69 <= i <= 80 and '@' <= ch <= 'p')
    return ''.join(ch for ch in s if ch not in to_filter)
