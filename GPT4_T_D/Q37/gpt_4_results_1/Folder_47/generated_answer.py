
def filter_chars(string):
    distinct_chars_to_remove = set([char for index, char in enumerate(string) if 38 <= index <= 54 and ':' <= char <= 'r'])
    new_string = ''
    for char in string:
        if char not in distinct_chars_to_remove:
            new_string += char
    return new_string
