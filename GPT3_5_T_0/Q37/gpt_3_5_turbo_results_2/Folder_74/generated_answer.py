
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 19 <= i <= 32 and 'f' <= char <= 'o':
            continue
        filtered_string += char
    return filtered_string
