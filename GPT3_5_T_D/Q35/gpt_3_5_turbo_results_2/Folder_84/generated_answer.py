
def remove_repeat_chars(string):
    repeat_chars = []
    for char in string[32:44]:
        if string.count(char) > 1:
            repeat_chars.append(char)
    
    new_string = ""
    for char in string:
        if char not in repeat_chars:
            new_string += char
    
    return new_string
