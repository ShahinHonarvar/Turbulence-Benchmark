
def filter_chars(input_string):
    chars_to_remove = {ch for ch in input_string[588:648] if ',' < ch < 'c'}
    output_string = ''.join(ch for ch in input_string if ch not in chars_to_remove)
    return output_string
