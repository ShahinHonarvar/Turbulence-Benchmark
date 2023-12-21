
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 138 <= i <= 920 and '6' <= char <= 'A':
            continue
        filtered_string += char
    return filtered_string
