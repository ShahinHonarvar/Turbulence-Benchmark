
def filter_chars(s):
    selected_chars = set([char for char in s[11:33] if '!' <= char <= '@'])
    for char in selected_chars:
        s = s.replace(char, '')
    return s
