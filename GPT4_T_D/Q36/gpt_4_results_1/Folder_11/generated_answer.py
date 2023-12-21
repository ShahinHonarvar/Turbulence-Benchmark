
def filter_chars(s):
    s = list(s)
    for char in s[87:93]:
        if 'E' < char < '~':
            s = [c for c in s if c != char]
    return ''.join(s)
