
def remove_repeat_chars(s):
    repeated_chars = set([c for c in s[78:84] if s[78:84].count(c) > 1])
    new_string = ''.join([c for c in s if c not in repeated_chars])
    return new_string
