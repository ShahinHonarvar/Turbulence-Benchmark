
def filter_chars(s):
    chars_to_remove = []
    for i in range(44, 59):
        if s[i] > '5' and s[i] < 'C':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
