
def remove_repeat_chars(string):
    repeated_chars = set()
    for char in string[56:90]:
        if string.count(char) > 1:
            repeated_chars.add(char)
            
    new_string = ""
    for char in string:
        if char not in repeated_chars:
            new_string += char
            
    return new_string
