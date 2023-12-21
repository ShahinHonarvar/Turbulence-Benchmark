
def filter_chars(string):
    filtered_string = ""
    
    for index, char in enumerate(string):
        if 28 <= index <= 65 and 'O' <= char <= 'd':
            continue
        filtered_string += char
    
    return filtered_string
