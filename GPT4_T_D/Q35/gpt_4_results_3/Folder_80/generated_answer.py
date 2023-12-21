
def remove_repeat_chars(s):
    sublist = s[58:84]
    for char in sublist:
        if sublist.count(char) > 1:
            s = s.replace(char, '')
    return s
