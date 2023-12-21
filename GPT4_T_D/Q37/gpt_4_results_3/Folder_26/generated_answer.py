
def filter_chars(s):
    chars_to_remove = []
    for i in range(20, 63):
        if i < len(s) and s[i] >= 'i' and s[i] <= 'k':
            chars_to_remove.append(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
