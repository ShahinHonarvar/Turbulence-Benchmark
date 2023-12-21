
def filter_chars(string):
    filtered_string = ""
    for i, c in enumerate(string):
        if 69 <= i < 87 and '#' < c < 'L':
            continue
        else:
            filtered_string += c
    return filtered_string
