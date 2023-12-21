
def filter_chars(string):
    to_remove = set(string[42:67])
    filtered_string = ''.join(char for char in string if char not in to_remove)
    return filtered_string
