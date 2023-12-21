
def remove_repeat_chars(input_string):
    repeated_chars = []
    for char in set(input_string[104:802]):
        if input_string.count(char) > 1:
            repeated_chars.append(char)
            
    for char in repeated_chars:
        input_string = input_string.replace(char, '')
        
    return input_string
