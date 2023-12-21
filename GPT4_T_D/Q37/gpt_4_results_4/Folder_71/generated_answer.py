
def filter_chars(input_string):
    chars_to_remove = [char for index, char in enumerate(input_string) if 32 <= index <= 46 and '0' <= char <= 'k']
    output_string = ''.join([char for char in input_string if char not in chars_to_remove])
    return output_string
