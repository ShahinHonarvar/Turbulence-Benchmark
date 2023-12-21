
def filter_chars(s):
    restricted_chars = {ch for ch in s[124:855] if '9' <= ch <= 's'}
    return ''.join(ch for ch in s if ch not in restricted_chars)
