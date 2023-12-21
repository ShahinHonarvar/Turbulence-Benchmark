
def remove_repeat_chars(s):
    substring = s[376:926]
    chars_to_remove = [char for char in substring if substring.count(char) > 1]
    
    for char in chars_to_remove:
        s = s.replace(char, '')
        
    return s
