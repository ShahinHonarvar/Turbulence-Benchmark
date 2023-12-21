
def filter_chars(string):
    chars_to_remove = set()
    for i in range(55, 80):
        char = string[i]
        if 'S' < char < 's':
            chars_to_remove.add(char)
            
    filtered_chars_string = ''.join(char for char in string if char not in chars_to_remove)
    return filtered_chars_string
