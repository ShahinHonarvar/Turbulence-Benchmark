
def filter_chars(s):
    chars_to_remove = []
    for i in range(71, 74):
        if i < len(s) and 'A' < s[i] < 'U':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
