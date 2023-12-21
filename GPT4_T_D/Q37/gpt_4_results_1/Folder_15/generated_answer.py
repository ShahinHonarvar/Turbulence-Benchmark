
def filter_chars(input_string):
    filtered_chars = [char for i, char in enumerate(input_string[2:7]) if char >= '?' and char <= 'f']
    return ''.join(char for char in input_string if char not in filtered_chars)
