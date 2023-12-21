
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if (41 <= i <= 79) and ('f' <= char <= '|'):
            continue
        else:
            filtered_string += char
    return filtered_string
