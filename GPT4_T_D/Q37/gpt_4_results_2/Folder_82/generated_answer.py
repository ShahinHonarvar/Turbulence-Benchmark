
def filter_chars(s):
    filtered_chars = [c for c in s[12:26] if c >= 'P' and c <= 'x']
    result = ''.join([c for c in s if c not in filtered_chars])
    return result
