
def filter_chars(input_str):
    chars_to_remove = []
    for char in input_str[56:66]:
        if 'f' < char < '|':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        input_str = input_str.replace(char, '')
    return input_str
