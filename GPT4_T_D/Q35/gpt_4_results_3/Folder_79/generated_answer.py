
def remove_repeat_chars(s):
    temp_str = s[2:7]
    for char in temp_str:
        if temp_str.count(char) > 1:
            s = s.replace(char, '')
    return s
