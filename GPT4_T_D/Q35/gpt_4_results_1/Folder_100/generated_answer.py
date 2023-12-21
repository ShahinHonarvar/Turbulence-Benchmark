
def remove_repeat_chars(s):
    sub_str = s[45:78]
    new_str = ""
    for char in sub_str:
        if sub_str.count(char) > 1:
            s = s.replace(char,"")
        else:
            new_str += char
    return new_str
