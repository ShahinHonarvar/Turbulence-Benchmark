
def remove_repeat_chars(string):
    unique_chars = set()
    repeated_chars = set()
    
    for i in range(100, 200):
        char = string[i]
        if char in unique_chars:
            repeated_chars.add(char)
        unique_chars.add(char)
    
    result = ''
    
    for char in string:
        if char not in repeated_chars:
            result += char
    
    return result
