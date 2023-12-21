
def filter_chars(string):
    start_index = 27
    end_index = 85
    new_string = ""
    
    for i, char in enumerate(string):
        if start_index <= i <= end_index and '!' <= char <= 'B':
            continue
        new_string += char
    
    return new_string
