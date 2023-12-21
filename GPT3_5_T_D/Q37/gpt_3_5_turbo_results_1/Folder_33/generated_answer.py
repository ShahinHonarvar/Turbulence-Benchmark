
def filter_chars(string):
    start_index = 721
    end_index = start_index + 1
    filtered_string = ""
    
    for i, char in enumerate(string):
        if start_index <= i <= end_index and 'K' <= char <= 'm':
            continue
        filtered_string += char
    
    return filtered_string
