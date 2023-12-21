
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 36 <= i <= 79 and '2' <= char <= 's':
            continue
        filtered_string += char
    
    return filtered_string
