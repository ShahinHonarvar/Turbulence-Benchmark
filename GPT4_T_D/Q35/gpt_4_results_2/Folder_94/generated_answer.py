
def remove_repeat_chars(s):
    remove_chars = set([c for c in s[43:87] if s[43:87].count(c) > 1])
    return "".join([c for c in s if c not in remove_chars])
