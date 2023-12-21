
def remove_repeat_chars(s):
    unique_chars = set(s[356:988])
    repeat_chars = [c for c in unique_chars if s[356:988].count(c) > 1]
    
    for char in repeat_chars:
        s = s.replace(char, '')
    
    return s
