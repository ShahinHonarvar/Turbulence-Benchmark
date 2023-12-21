
def filter_chars(in_str):
    chars_to_remove = [char for char in in_str[477:985] if ',' <= char <= 'V']
    out_str = ''.join([char for char in in_str if char not in chars_to_remove])
    
    return out_str
