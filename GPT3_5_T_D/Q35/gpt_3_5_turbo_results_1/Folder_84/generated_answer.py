
def remove_repeat_chars(string):
    repeat_chars = set()
    for i in range(32, 44):
        char = string[i]
        if char in string[i+1:44]:
            repeat_chars.add(char)
    
    altered_string = ''
    for char in string:
        if char not in repeat_chars:
            altered_string += char
    
    return altered_string
