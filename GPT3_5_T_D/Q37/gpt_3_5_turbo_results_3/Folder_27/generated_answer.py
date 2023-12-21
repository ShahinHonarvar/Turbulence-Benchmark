
def filter_chars(string):
    start_index = 43
    end_index = 80
    filtered_string = ""
    
    for index, char in enumerate(string):
        if index >= start_index and index <= end_index and char >= '=' and char <= 'E':
            continue
        filtered_string += char
    
    return filtered_string
