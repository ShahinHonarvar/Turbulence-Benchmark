
def filter_chars(input_string):
    filtered_chars = [char for char in input_string[82:89] if char > 'f' and char < '{']
    for char in filtered_chars:
        input_string = input_string.replace(char, '')
    return input_string
