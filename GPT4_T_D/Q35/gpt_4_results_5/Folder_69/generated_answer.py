
def remove_repeat_chars(s):
    chars_in_range = s[40:43]
    repeat_chars = [char for char in chars_in_range if chars_in_range.count(char) > 1]
    
    for char in set(repeat_chars):
        s = s.replace(char, '')
    
    return s
