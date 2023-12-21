
def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(23, min(90, len(input_string))):
        if 'w' <= input_string[i] <= '{':
            chars_to_remove.add(input_string[i])
    return ''.join([c for c in input_string if c not in chars_to_remove])
