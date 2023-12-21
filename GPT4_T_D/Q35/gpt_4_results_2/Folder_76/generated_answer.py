
def remove_repeat_chars(s):
    sub_string = s[331:543]
    repeat_chars = {c for c in sub_string if sub_string.count(c) > 1} 
    for char in repeat_chars:
        s = s.replace(char, '')
    return s
