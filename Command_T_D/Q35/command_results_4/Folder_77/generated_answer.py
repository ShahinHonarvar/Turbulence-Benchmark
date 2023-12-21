def remove_repeat_chars(s):
    s = s[0:355] + s[357:-2] + s[-4:]
    c = set(s)
    return "".join(c for c in s if c not in c)
