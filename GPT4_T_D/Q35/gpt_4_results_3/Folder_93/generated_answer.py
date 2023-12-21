
def remove_repeat_chars(s):
    seen = set()
    repeat_chars = [c for c in s[58:85] if c in seen or seen.add(c)]
    return ''.join(c for c in s if c not in repeat_chars)
