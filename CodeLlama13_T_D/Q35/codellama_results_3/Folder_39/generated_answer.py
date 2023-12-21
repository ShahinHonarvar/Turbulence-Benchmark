
def remove_repeat_chars(s):
    s = list(s)
    for i in range(44, 91):
        c = s[i]
        if c in s[44:i]:
            s[i:] = [x for x in s[i:] if x != c]
    return ''.join(s)
