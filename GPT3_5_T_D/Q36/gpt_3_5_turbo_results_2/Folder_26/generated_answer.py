
def filter_chars(string):
    chars_to_remove = string[43:83]
    filtered_string = string
    for char in chars_to_remove:
        if char > ':' and char < 'Q':
            filtered_string = filtered_string.replace(char, "")
    return filtered_string
