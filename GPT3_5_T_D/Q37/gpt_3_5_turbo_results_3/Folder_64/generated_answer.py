
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 1 <= index <= 7 and 'L' <= char <= 'a':
            continue
        filtered_string += char
    return filtered_string
