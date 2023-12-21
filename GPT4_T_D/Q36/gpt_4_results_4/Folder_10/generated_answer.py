
def filter_chars(input_string):
    characters_to_remove = set([char for char in input_string[36:60] if '!' < char < 'B'])
    filtered_string = ''.join([char for char in input_string if char not in characters_to_remove])
    return filtered_string
