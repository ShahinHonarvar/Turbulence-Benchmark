
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 19 and i <= 90 and char >= 'F' and char <= 'h':
            continue
        filtered_string += char
    return filtered_string
