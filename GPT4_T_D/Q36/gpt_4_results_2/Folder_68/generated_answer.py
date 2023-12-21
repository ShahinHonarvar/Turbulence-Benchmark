
def filter_chars(s):
    chars_to_remove = []
    for i in range(2,9):
        if s[i] > '8' and s[i] < 'm':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
