
def filter_chars(s):
    filtered = [c for c in s[34:68] if c >= 'W' and c <= 'x']
    return ''.join(char for char in s if char not in filtered)
