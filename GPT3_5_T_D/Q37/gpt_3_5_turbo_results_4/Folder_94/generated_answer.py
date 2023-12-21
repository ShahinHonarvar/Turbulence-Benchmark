
def filter_chars(string):
    filtered_string = ""
    
    for i, char in enumerate(string):
        if i < 51 or i > 96 or char < 'X' or char > 'p':
            filtered_string += char
    
    return filtered_string
