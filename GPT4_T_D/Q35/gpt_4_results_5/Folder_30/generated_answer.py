
def remove_repeat_chars(s):
    between_indices = s[23:24]
    repeat_chars = [char for char in between_indices if between_indices.count(char) > 1]
    
    for char in repeat_chars:
        s = s.replace(char, '')
    
    return s
