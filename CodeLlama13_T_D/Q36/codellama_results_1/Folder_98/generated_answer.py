
def filter_chars(s):
    chars = set()
    for i in range(4, 8):
        if s[i].isalpha() and s[i] > '1' and s[i] < 'J':
            chars.add(s[i])
    return ''.join([c for c in s if c not in chars])
