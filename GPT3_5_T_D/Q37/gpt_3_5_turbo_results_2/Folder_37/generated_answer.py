
def filter_chars(string):
    filtered_str = ''
    for index, char in enumerate(string):
        if 17 <= index <= 63 and 'O' <= char <= '^':
            continue
        filtered_str += char
    return filtered_str
