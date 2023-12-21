
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 513 <= index <= 877 and '?' <= char <= 'n':
            continue
        filtered_string += char
    return filtered_string
