
def filter_chars(input_string):
    chars_to_remove = [ch for ch in input_string[70:87] if '#' < ch < 'L']
    for ch in set(chars_to_remove):
        input_string = input_string.replace(ch, '')
    return input_string
