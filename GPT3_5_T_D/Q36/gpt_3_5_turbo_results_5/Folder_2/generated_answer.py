
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 421 or i >= 854 or string[i] <= 'D' or string[i] >= 'J':
            filtered_string += string[i]
    
    return filtered_string
