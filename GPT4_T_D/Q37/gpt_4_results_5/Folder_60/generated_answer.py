
def filter_chars(input_string):
    chars_to_remove = [char for idx, char in enumerate(input_string) if 12 <= idx <= 77 and ':' <= char <= 'L']
    output_string = ''.join(char for char in input_string if char not in chars_to_remove)
    return output_string
