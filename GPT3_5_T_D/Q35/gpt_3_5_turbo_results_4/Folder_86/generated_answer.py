
def remove_repeat_chars(string):
    unique_chars = set()
    repeated_chars = set()
    
    for i in range(19, 32):
        if string[i] in unique_chars:
            repeated_chars.add(string[i])
        else:
            unique_chars.add(string[i])
    
    result = ""
    for char in string:
        if char not in repeated_chars:
            result += char
    
    return result
