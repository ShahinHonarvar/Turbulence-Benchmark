
def remove_repeat_chars(s):
    substring = s[17:87]
    chars_repeated = [c for c in set(substring) if substring.count(c) > 1]
    return "".join(c for c in s if c not in chars_repeated)
