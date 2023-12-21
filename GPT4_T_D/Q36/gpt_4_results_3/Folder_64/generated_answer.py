
def filter_chars(input_str):
    chars_to_remove = [ch for ch in input_str[2:7] if '3' < ch < '^']
    for char in chars_to_remove:
        input_str = input_str.replace(char, '')
    return input_str
