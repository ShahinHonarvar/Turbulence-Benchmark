
def filter_chars(input_string):
    characters_to_remove = set([char for index, char in enumerate(input_string) if 477 <= index <= 984 and ',' <= char <= 'V'])
    return ''.join([char for char in input_string if char not in characters_to_remove])
