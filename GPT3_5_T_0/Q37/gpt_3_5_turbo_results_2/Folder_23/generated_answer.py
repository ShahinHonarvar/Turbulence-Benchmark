
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 51 <= i <= 77 and 'V' <= char <= 'Y':
            continue
        filtered_string += char
    return filtered_string
