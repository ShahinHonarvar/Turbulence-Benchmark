
def remove_repeat_chars(s):
    repeat_chars = set([c for c in s[477:709] if s[477:709].count(c) > 1])
    return ''.join([c for i, c in enumerate(s) if c not in repeat_chars])
