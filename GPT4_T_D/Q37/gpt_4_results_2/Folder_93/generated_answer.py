
def filter_chars(s):
    sub_str = s[38:70]
    chars_to_remove = [char for char in sub_str if 'H' <= char <= 'e']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
