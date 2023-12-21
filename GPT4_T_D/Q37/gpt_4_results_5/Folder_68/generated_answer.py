
def filter_chars(s):
    chars_to_remove = []
    for i in range(7, 10):
        if i < len(s) and s[i] >= '6' and s[i] <= 'w':
            chars_to_remove.append(s[i])

    for char in chars_to_remove:
        s = s.replace(char, '')

    return s
