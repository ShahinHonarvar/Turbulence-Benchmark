
def filter_chars(string):
    filtered_string = ''
    for char in string:
        if len(filtered_string) < 36 or len(filtered_string) > 79:
            filtered_string += char
        elif char >= 'a' and char <= 'i':
            filtered_string += char
    return filtered_string
