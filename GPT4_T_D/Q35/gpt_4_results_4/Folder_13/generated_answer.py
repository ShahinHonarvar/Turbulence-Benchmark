
def remove_repeat_chars(s):
    subset = s[47:91]
    for char in subset:
        if subset.count(char) > 1:
            s = s.replace(char, '')
    return s
