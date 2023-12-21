import itertools
def remove_repeat_chars(s):
    i = 0
    j = 0
    for c in itertools.groupby(s):
        if len(list(c)) > 2:
            s = s.replace(c, '')
        else:
            j += 1
            s = s[i:j]
            i = j
    return s
