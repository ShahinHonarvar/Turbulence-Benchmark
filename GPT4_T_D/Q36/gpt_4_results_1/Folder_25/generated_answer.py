
def filter_chars(input_str):
    selected_chars = [ch for ch in input_str[25:37] if 'A' < ch < 'h']
    return ''.join(ch for ch in input_str if ch not in selected_chars)
