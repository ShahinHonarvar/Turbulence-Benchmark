
def filter_chars(input_string):
    filtered_string = input_string[:]
    for char in input_string[344:665]:
        if '%' < char < 'U':
            filtered_string = filtered_string.replace(char, '')
    return filtered_string
