
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 7 <= i <= 9 and '6' <= char <= 'w':
            continue
        filtered_string += char
    return filtered_string
