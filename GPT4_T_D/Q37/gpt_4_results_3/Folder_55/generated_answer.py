
def filter_chars(s):
    chars_to_remove = [c for c in s[1:6] if '$' <= c <= ';']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
