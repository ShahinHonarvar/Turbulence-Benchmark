def remove_repeat_chars(s):
    c = set()
    for i in range(len(s) - 3):
        c.add(s[i])
    return ''.join(x for x in s if x in c)
