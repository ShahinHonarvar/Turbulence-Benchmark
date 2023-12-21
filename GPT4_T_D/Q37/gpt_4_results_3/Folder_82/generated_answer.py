
def filter_chars(input_string):
    to_filter = [ch for ch in input_string[12:26] if 'P' <= ch <= 'x']
    return ''.join(ch for ch in input_string if ch not in to_filter)
