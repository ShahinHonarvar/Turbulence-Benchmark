
def filter_chars(input_str):
    boundary_chars = input_str[83:89]
    for char in boundary_chars:
        if '*'<char<'[':
            input_str = input_str.replace(char,'')
    return input_str
