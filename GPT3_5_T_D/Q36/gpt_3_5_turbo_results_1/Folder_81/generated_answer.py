
def filter_chars(string):
    filtered_string = string[:51] + string[76:]
    char_to_remove = [char for char in string[51:76] if '5' < char < 'f']
    for char in char_to_remove:
        filtered_string = filtered_string.replace(char, "")
    return filtered_string
