
def filter_chars(s):
    chars_to_remove = []
    for i in range(4, 5):
        if s[i] > 'Y' and s[i] < 's':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
