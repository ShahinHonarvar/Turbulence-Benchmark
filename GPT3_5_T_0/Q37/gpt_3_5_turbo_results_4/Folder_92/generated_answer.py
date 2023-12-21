
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 4 and i <= 4 and char >= '7' and char <= 'o':
            continue
        filtered_string += char
    return filtered_string
