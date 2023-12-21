
def filter_chars(s):
    chars_filter = [c for c in s[1:6] if '$' <= c <= ';']
    return "".join(c for c in s if c not in chars_filter)
