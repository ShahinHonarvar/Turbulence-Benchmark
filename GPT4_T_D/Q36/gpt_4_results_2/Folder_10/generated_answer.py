
def filter_chars(s):
    chars_to_remove = []
    for i, c in enumerate(s):
        if 35 < i < 60 and '!' < c < 'B':
            chars_to_remove.append(c)
    return ''.join(char for char in s if char not in chars_to_remove)
