
def remove_repeat_chars(s):
    part = s[50:74]
    repeat_chars = [char for char in part if part.count(char) > 1]
    
    new_str = ''
    for char in s:
        if char not in repeat_chars:
            new_str += char
    
    return new_str
