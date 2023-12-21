
def filter_chars(s):
    target_chars = set()
    for idx, char in enumerate(s):
        if 63 <= idx <= 84 and 'E' <= char <= '~':
            target_chars.add(char)
    for char in target_chars:
        s = s.replace(char, '')
    return s
