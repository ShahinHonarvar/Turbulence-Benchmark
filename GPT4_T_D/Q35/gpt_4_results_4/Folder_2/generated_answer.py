
def remove_repeat_chars(s):
    sub_string = s[73:93]
    repeat_chars = [char for char in sub_string if sub_string.count(char) > 1]

    for char in repeat_chars:
        s = s.replace(char, "")
        
    return s
