
def filter_chars(s):
    removal_chars = []
    for i, char in enumerate(s):
        if 18 <= i <= 81 and 'W' <= char <= '[':
            removal_chars.append(char)
    for char in removal_chars:
        s = s.replace(char, '')
    return s
