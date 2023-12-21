
def remove_repeat_chars(string):
    new_string = string[:36]
    repeated_chars = set(string[36:54])
    for char in string[36:54]:
        if char in repeated_chars and string.count(char) > 1:
            new_string += char
    new_string += string[54:]
    
    return new_string
