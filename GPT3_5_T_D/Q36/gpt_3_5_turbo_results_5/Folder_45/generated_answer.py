
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 81 <= i < 86 and '!' < char < 's':
            continue
        filtered_string += char
    return filtered_string
