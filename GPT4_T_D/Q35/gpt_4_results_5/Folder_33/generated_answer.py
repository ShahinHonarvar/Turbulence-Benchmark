
def remove_repeat_chars(s):
    subset = s[126:825]
    to_remove = set(x for x in subset if subset.count(x) > 1)
    return ''.join(x for x in s if x not in to_remove)
