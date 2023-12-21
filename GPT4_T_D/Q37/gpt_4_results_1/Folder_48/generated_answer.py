
def filter_chars(s):
    valid_chars = [ch for ch in s[513:878] if '?' <= ch <= 'n']
    return ''.join(ch for ch in s if ch not in valid_chars)
