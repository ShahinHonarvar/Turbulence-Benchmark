
def filter_chars(input_string):
    removed_chars = [ch for ch in input_string[33:84] if 'm' < ch < 'w']

    for char in removed_chars:
        input_string = input_string.replace(char, '')
        
    return input_string
