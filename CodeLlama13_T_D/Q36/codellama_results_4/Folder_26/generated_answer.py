
def filter_chars(s):
    chars = []
    for i in range(43, 83):
        if s[i].isalpha() and ':' < s[i] < 'Q':
            chars.append(s[i])
    return "".join([c for c in s if c not in chars])
