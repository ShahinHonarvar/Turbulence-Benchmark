
def filter_chars(input_string):
    filtered_string = ""
    for char in input_string[46:57]:
        if 'F' < char < 'n':
            input_string = input_string.replace(char, '')
    return input_string
