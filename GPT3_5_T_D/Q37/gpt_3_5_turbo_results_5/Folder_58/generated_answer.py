
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 503 <= i <= 753 and '9' <= char <= 'w':
            continue
        filtered_string += char
    return filtered_string
