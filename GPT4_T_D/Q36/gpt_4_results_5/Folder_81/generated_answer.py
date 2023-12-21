
def filter_chars(s):
    charsToRemove = []
    for i in s[52:76]:
        if i > '5' and i < 'f':
            charsToRemove.append(i)
    for char in charsToRemove:
        s = s.replace(char, '')
    return s
