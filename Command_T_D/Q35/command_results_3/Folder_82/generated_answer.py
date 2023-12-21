import itertools
def remove_repeat_chars(s):
    r = ""
    for i in range(30, 200):
        r += s[i]
        if r in s:
            r = ""
    return r
