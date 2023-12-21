
def filter_chars(string):
    filtered_string = string[:57]
    for char in string[57:69]:
        if char > '(' and char < 'W':
            filtered_string = filtered_string.replace(char, '')
    filtered_string += string[69:]
    return filtered_string
