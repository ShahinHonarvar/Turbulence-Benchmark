
def filter_chars(s):
    chars = []
    for i in range(15, 56):
        if s[i].isalpha() and ord(s[i]) >= ord('W') and ord(s[i]) <= ord('{'):
            chars.append(s[i])
    return ''.join([c for c in s if c not in chars])
