
def filter_chars(input_str):
    filtered_str = input_str
    range_chars = input_str[25:37]
    
    for char in range_chars:
        if 'A' < char < 'h':
            filtered_str = filtered_str.replace(char, '')
    
    return filtered_str
