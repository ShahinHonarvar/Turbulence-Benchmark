
def remove_repeat_chars(s):
    s = list(s)
    repeat_chars = set([c for c in s[356:988] if s[356:988].count(c) > 1])
    return ''.join([c for c in s if c not in repeat_chars])
