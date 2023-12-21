
def filter_chars(string):
    new_string = ""
    for i, char in enumerate(string):
        if 35 <= i <= 98 and 'A' <= char <= 'b':
            continue
        else:
            new_string += char
    return new_string
