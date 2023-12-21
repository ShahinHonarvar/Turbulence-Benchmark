
def filter_chars(input_string):
    chars_to_remove = set([char for i, char in enumerate(input_string) 
                           if 41 <= i <= 79 and 'f' <= char <= '|'])
    output_string = ''.join([char for char in input_string if char not in chars_to_remove])
    return output_string
