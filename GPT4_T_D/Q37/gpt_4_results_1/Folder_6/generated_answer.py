
def filter_chars(my_str):
    new_string = ''
    chars_to_remove = set([char for i, char in enumerate(my_str) if 13 <= i <= 28 and 'c' <= char <= 'n'])
    for char in my_str:
        if char not in chars_to_remove:
            new_string += char
    return new_string
