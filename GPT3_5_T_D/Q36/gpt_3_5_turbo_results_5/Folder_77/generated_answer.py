
def filter_chars(string):
    filtered_string = ""
    
    for i, char in enumerate(string):
        if 221 <= i < 419 and '-' < char < 'v':
            continue
        filtered_string += char
    
    return filtered_string
