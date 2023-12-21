
def filter_chars(string):
    filtered_string = ""
    
    for i in range(len(string)):
        if i >= 54 and i <= 62 and string[i] >= ')' and string[i] <= '9':
            continue
        else:
            filtered_string += string[i]
    
    return filtered_string
