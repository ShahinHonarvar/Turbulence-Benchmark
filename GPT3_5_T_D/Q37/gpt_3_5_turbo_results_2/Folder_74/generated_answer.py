
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 19 and i <= 32 and char >= 'f' and char <= 'o':
            continue
        filtered_string += char
    return filtered_string
