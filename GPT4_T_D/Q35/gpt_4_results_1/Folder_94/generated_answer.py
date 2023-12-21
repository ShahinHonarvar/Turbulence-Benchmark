
def remove_repeat_chars(s):
    sub_string = s[43:87]
    unique_chars = set(sub_string)
    repeated_chars = [char for char in unique_chars if sub_string.count(char) > 1]
    
    for repeated_char in repeated_chars:
        s = s.replace(repeated_char, '')
        
    return s
