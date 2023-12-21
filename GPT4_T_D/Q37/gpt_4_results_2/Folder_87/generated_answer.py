
def filter_chars(s):
    filtered_chars = [c for c in s[18:82] if c >= 'W' and c <= '[']
    return ''.join(c for c in s if c not in filtered_chars)
