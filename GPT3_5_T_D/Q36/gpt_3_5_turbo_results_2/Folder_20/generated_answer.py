
def filter_chars(string):
    filtered_string = string[:13]
    filtered_string += string[40:]
    
    for char in string[13:40]:
        if char > ':' and char < 'C':
            filtered_string = filtered_string.replace(char, '')
    
    return filtered_string
