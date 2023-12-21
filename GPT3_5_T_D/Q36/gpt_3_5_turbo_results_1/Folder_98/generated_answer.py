
def filter_chars(string):
    chars_to_remove = set()
    for i in range(4, 8):
        if '1' < string[i] < 'J':
            chars_to_remove.add(string[i])
    
    filtered_string = ""
    for char in string:
        if char not in chars_to_remove:
            filtered_string += char
    
    return filtered_string
