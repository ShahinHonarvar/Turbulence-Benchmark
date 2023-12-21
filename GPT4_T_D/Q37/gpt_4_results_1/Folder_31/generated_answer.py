
def filter_chars(s):
    chars_to_remove = set(s[i] for i in range(57, min(97, len(s))) if '<' <= s[i] <= 'w')
    return ''.join(c for c in s if c not in chars_to_remove)
