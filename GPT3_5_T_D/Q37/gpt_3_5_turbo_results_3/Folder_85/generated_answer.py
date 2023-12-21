
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 28 and i <= 65 and char >= 'O' and char <= 'd':
            continue
        filtered_string += char
    return filtered_string
