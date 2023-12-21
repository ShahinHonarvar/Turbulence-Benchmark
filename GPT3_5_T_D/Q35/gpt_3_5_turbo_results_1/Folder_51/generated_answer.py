
def remove_repeat_chars(s):
    repeat_chars = set()
    
    for char in s[6:9]:
        if s.count(char) > 1:
            repeat_chars.add(char)
    
    new_string = ""
    for char in s:
        if char not in repeat_chars:
            new_string += char
    
    return new_string
