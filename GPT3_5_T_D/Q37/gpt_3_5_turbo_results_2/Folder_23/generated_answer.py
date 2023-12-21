
def filter_chars(string):
    chars_to_remove = set()
    
    for index, char in enumerate(string):
        if 51 <= index <= 77 and 'V' <= char <= 'Y':
            chars_to_remove.add(char)
    
    return ''.join(char for char in string if char not in chars_to_remove)
