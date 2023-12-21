
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 515 <= i <= 538 and '+' <= char <= '}':
            continue
        filtered_string += char
    return filtered_string
