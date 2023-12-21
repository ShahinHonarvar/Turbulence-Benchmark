
def filter_chars(str_input):
    chars_in_range = [c for c in str_input[284:484] if 'l'<c<'t']
    return ''.join(c for c in str_input if c not in chars_in_range)
