
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 24 <= i <= 79 and 'a' <= char <= 'f':
            continue
        filtered_string += char
    return filtered_string
