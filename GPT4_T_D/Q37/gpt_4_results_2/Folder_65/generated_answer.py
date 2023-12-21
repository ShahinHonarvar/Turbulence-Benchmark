
def filter_chars(s):
    special_chars = set(s[i] for i in range(61, min(71, len(s))) if '0' <= s[i] <= '@')
    return ''.join(char for char in s if char not in special_chars)
