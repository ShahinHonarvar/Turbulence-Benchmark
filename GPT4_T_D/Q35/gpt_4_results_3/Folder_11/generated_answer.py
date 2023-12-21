
def remove_repeat_chars(s):
    s = list(s)
    repeated_chars = [char for char in set(s[49:76]) if s[49:76].count(char) > 1]
    
    for repeated_char in repeated_chars:
        while repeated_char in s:
            s.remove(repeated_char)
            
    return "".join(s)
