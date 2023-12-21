
def remove_repeat_chars(string):
    unique_chars = set()
    repeated_chars = set()
    altered_string = ""
    
    for i, char in enumerate(string):
        if 34 < i < 69:
            if char in unique_chars:
                repeated_chars.add(char)
            else:
                unique_chars.add(char)

    for char in string:
        if char not in repeated_chars:
            altered_string += char
    
    return altered_string
