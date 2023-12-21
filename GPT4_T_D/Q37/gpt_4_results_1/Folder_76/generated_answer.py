
def filter_chars(s):
    if not s:
        return s
    part_string = s[379:899]
    chars_to_remove = [ch for ch in part_string if 'M' <= ch <= 'v']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
