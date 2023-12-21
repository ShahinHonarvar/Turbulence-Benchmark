
def filter_chars(input_string):
    to_remove = []
    for idx, char in enumerate(input_string):
        if 11 <= idx <= 72 and 'i' <= char <= 'v':
            to_remove.append(char)

    for char in to_remove:
        input_string = input_string.replace(char, '')

    return input_string
