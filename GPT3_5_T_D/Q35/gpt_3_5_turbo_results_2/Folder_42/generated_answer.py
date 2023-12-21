
def remove_repeat_chars(s):
    for char in s[18:60]:
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s
