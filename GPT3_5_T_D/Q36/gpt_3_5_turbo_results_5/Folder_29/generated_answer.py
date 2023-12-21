
def filter_chars(string):
    filtered_string = string[:46] + string[68:]
    chars_to_remove = [char for char in string[46:68] if 'H' < char < 's']
    for char in chars_to_remove:
        filtered_string = filtered_string.replace(char, '')
    return filtered_string
