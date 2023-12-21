
def filter_chars(string):
    start_index = 34
    end_index = 67
    filtered_string = ""
    
    for i in range(len(string)):
        if i >= start_index and i <= end_index:
            if string[i] >= 'W' and string[i] <= 'x':
                continue
        filtered_string += string[i]
    
    return filtered_string
