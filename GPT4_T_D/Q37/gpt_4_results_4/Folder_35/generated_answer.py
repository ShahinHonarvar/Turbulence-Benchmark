
def filter_chars(string):
    filtered_chars = [char for char in string[155:404] if '(' <= char <= ']']
    return ''.join([char for char in string if char not in filtered_chars])
