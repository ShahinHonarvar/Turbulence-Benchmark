
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 373 <= i <= 901 and 'T' <= char <= 'h':
            continue
        filtered_string += char
    return filtered_string
