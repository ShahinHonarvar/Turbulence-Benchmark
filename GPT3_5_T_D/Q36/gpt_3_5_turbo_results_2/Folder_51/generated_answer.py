
def filter_chars(string):
    filtered_string = ''
    for i, c in enumerate(string):
        if 58 <= i < 81:
            if '5' < c < '>':
                continue
        filtered_string += c
    return filtered_string
