 
def filter_chars(string):
    if len(string) < 6:
        return string
    
    chars_to_remove = set()
    for i in range(3, 5):
        if ord(string[i]) > ord('Y') and ord(string[i]) < ord('s'):
            chars_to_remove.add(string[i])
    
    filtered_string = ""
    for char in string:
        if char not in chars_to_remove:
            filtered_string += char
    
    return filtered_string
