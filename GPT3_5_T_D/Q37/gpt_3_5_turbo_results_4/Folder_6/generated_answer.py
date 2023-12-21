
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 13 and i <= 28 and char >= 'c' and char <= 'n':
            continue
        filtered_string += char
    return filtered_string
