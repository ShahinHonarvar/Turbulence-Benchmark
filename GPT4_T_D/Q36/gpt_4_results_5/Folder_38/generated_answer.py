
def filter_chars(input_string):
    chars_to_remove = [ch for ch in input_string[45:48] if '+' < ch < 'l']
    for ch in chars_to_remove:
        input_string = input_string.replace(ch, '')
    return input_string
