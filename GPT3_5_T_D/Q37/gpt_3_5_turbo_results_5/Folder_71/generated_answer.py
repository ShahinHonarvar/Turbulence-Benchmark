
def filter_chars(string):
    filtered_string = string
    for i in range(32, 47):
        char = chr(i)
        if char >= '0' and char <= 'k':
            filtered_string = filtered_string.replace(char, '')
    return filtered_string
