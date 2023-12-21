
def filter_chars(s):
    chars_to_remove = set([c for c in s[1:8] if 'L' <= c <= 'a'])
    new_s = "".join([c for c in s if c not in chars_to_remove])
    return new_s
