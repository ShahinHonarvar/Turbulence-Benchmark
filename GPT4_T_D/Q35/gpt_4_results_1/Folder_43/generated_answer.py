
def remove_repeat_chars(s):
    ctr = {}
    for i in range(11, min(28, len(s))):
        ctr[s[i]] = ctr.get(s[i], 0) + 1
    return ''.join(c for i, c in enumerate(s) if ctr.get(c, 0) < 2)
