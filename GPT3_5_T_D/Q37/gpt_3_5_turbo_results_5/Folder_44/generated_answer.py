
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 21 <= i <= 43 and '+' <= char <= '8':
            continue
        filtered_string += char
    return filtered_string
