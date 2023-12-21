
def filter_chars(s):
    substring = s[1:6]
    characters_to_remove = [c for c in substring if '$' <= c <= ';']
    return ''.join(c for c in s if c not in characters_to_remove)
