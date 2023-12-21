
def remove_repeat_chars(s):
    substring = s[26:80]
    unique_chars = set(substring)
    remove_chars = [c for c in unique_chars if substring.count(c) > 1]
    return ''.join([c for c in s if c not in remove_chars])
