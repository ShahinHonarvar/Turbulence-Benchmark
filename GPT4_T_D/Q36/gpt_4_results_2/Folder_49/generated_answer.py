
def filter_chars(input_str):
    chars_to_remove = {ch for ch in input_str[47:91] if 'D' < ch < 'H'}
    return ''.join(ch for ch in input_str if ch not in chars_to_remove)
