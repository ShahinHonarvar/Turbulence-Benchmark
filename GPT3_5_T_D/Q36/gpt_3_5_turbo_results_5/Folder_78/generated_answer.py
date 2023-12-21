
def filter_chars(string):
    chars_to_remove = string[29:33]
    filtered_string = ''
    for char in string:
        if char in chars_to_remove and '%' < char < 'a':
            continue
        filtered_string += char
    return filtered_string
