
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 37 <= i <= 56 and '6' <= char <= '_':
            continue
        filtered_string += char
    return filtered_string
