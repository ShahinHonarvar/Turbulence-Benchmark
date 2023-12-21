
def filter_chars(s):
    
    chars_to_remove = []
    for char in s[300:418]:
        if char > '9' and char < 'P':
            chars_to_remove.append(char)
    
    for char_to_remove in chars_to_remove:
        s = s.replace(char_to_remove, '')
    return s
