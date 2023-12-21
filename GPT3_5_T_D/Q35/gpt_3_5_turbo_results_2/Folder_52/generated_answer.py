
def remove_repeat_chars(string):
    new_string = ''
    repeat_chars = set()
    
    for i in range(38, 81):
        if string[i] in repeat_chars:
            continue
        elif string.count(string[i], 38, 81) > 1:
            repeat_chars.add(string[i])
    
    for char in string:
        if char not in repeat_chars:
            new_string += char
    
    return new_string
