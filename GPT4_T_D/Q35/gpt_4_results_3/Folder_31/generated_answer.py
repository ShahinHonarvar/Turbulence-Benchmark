
def remove_repeat_chars(s):
    if len(s) > 78:
        sub_string = s[34:78]
        for char in sub_string:
            if sub_string.count(char) > 1:
                s = s.replace(char, '')
    return s
