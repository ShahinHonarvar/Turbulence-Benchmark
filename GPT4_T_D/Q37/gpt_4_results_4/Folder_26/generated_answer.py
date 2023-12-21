
def filter_chars(s):
    to_remove = [ch for ch in s[20:63] if 'i' <= ch <= 'k']
    return ''.join(ch for ch in s if ch not in to_remove)
