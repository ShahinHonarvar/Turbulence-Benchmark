
def filter_chars(string):
    filtered_string = string[:44]
    filtered_string += string[68:]
    
    for char in string[44:68]:
        if 'W' < char < 'x':
            filtered_string = filtered_string.replace(char, '')

    return filtered_string
