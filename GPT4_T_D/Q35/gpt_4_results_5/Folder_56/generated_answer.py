
def remove_repeat_chars(s):
    temp = s[8:9]
    for char in temp:
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s
