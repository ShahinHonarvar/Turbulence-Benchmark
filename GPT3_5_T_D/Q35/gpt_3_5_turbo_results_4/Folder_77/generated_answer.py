
def remove_repeat_chars(string):
    modified_string = ''
    repeat_chars = set()
    
    for i in range(355, 988):
        char = string[i]
        if char in repeat_chars:
            modified_string = modified_string.replace(char, '')
        else:
            repeat_chars.add(char)
            modified_string += char
    
    return modified_string
