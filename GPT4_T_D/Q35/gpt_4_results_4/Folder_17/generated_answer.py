
def remove_repeat_chars(s):
    if len(s) > 85:
        for char in set(s[74:84]):
            if s[74:84].count(char) > 1:
                s = s.replace(char, '')
    return s
