
def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s) if i > 61 and i < 88 and '%' < c < 'q']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
