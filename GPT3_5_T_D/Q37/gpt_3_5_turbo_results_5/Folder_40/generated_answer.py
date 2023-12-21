
def filter_chars(s):
    chars_to_remove = []
    for char in s[0:2]:
        if '*' <= char <= 's':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
