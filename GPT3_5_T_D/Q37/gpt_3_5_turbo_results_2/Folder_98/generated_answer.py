
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 8 and i <= 9:
            if char >= 'R' and char <= 't':
                continue
        filtered_string += char
    return filtered_string
