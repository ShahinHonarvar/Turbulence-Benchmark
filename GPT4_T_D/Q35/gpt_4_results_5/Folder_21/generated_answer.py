
def remove_repeat_chars(s):
    restrict = s[463:995]
    for char in set(restrict):
        if restrict.count(char) > 1:
            s = s.replace(char, '')
    return s
