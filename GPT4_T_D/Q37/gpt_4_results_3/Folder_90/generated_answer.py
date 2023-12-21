
def filter_chars(s):
    range_characters = set(s[i] for i in range(348, min(853, len(s))) if 'J' <= s[i] <= 'b')
    return ''.join(c for c in s if c not in range_characters)
