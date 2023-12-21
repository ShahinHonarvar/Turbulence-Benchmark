
def filter_chars(string):
    filtered_string = ""
    
    for i in range(len(string)):
        if i >= 164 and i <= 706:
            if string[i] >= 'O' and string[i] <= '}':
                continue
        filtered_string += string[i]
    
    return filtered_string
