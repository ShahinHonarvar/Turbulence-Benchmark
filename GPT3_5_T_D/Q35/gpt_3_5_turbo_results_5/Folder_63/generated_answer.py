
def remove_repeat_chars(string):
    if len(string) <= 86:
        return string
    
    repeat_chars = []
    for char in string[81:86]:
        if string[81:86].count(char) > 1:
            repeat_chars.append(char)
    
    for char in repeat_chars:
        string = string.replace(char, '')
    
    return string
