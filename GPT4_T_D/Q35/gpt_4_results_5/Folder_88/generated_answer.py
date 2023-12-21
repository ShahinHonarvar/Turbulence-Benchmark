
def remove_repeat_chars(s):
    sub_string = s[4:9]
    for char in sub_string:
        if sub_string.count(char) > 1:
            s = s.replace(char, "")
    return s
