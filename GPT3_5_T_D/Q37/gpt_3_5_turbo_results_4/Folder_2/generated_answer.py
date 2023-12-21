
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 477 <= i <= 984 and ',' <= char <= 'V':
            continue
        filtered_string += char
    return filtered_string
