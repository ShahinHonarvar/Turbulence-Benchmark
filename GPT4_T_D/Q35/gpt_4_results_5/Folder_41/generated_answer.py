
def remove_repeat_chars(s):
    check = s[4:8]
    for char in check:
        if check.count(char) > 1:
            s = s.replace(char, '')
    return s
