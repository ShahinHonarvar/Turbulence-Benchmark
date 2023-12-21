
def remove_repeat_chars(s):
    chars_in_range = s[44:70]
    repeat_chars = [c for c in set(chars_in_range) if chars_in_range.count(c) > 1]
    
    new_string = ""
    for c in s:
        if c not in repeat_chars:
            new_string += c
            
    return new_string
