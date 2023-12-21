
def filter_chars(s):
    substr = s[586:648]
    chars_to_remove = [ch for ch in substr if ',' < ch < 'c']
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s
