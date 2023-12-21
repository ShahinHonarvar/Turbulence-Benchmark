
def remove_repeat_chars(s):
    sub = s[1:9]
    for char in sub:
        if sub.count(char) > 1:
            s = s.replace(char, '')
    return s
