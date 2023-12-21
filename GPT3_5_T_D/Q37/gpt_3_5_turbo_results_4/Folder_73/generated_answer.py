
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 22 <= i <= 85 and '7' <= char <= 'e':
            continue
        filtered_string += char
    return filtered_string
