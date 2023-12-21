
def filter_chars(string):
    characters_to_remove = set([char for char in string[7:9] if 'B' <= char <= 'H'])
    return ''.join([char for char in string if char not in characters_to_remove])
