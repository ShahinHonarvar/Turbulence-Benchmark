
def remove_repeat_chars(s):
    repeated_chars = set([c for c in s[36:64] if s[36:64].count(c) > 1])
    return "".join([c for c in s if c not in repeated_chars])
