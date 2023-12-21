
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 86 and i <= 92 and char >= '!' and char <= 's':
            continue
        filtered_string += char
    return filtered_string
