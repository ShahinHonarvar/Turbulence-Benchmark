
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 71 <= i <= 94 and 'K' <= char <= 'a':
            continue
        filtered_string += char
    return filtered_string
