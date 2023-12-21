
def remove_repeat_chars(s):
    duplicate_chars = set([c for c in s[73:93] if s[73:93].count(c)>1])
    return "".join([c for c in s if c not in duplicate_chars])
