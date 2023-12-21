
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 36 <= i <= 40 and 'H' <= char <= 'e':
            continue
        filtered_string += char
    return filtered_string
