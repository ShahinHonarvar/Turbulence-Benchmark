
def filter_chars(string):
    filtered_string = string[:82]
    remaining_string = string[82:89]
    remaining_chars = [char for char in remaining_string if char <= '*' or char >= '[']
    filtered_string += remaining_chars + string[89:]
    return filtered_string
