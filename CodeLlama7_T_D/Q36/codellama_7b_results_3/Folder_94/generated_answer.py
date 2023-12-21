
def filter_chars(s):
    # create a list of characters that should be removed
    chars_to_remove = []
    for i in range(15, 86):
        if s[i] > 'I' and s[i] < 'M':
            chars_to_remove.append(s[i])
    # remove the characters from the string
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
