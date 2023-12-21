
def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(19, 32):
        char = string[i]
        if char in string[i+1:32]:
            repeated_chars.add(char)
    
    new_string = ""
    for char in string:
        if char not in repeated_chars:
            new_string += char
    
    return new_string
