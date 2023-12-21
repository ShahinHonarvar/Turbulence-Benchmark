
def remove_repeat_chars(s):
    slice = s[56:84]
    for char in slice:
        if slice.count(char) > 1:
            s = s.replace(char, '')
    return s
