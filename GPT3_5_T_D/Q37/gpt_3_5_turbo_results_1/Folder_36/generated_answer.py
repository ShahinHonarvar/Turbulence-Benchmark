
def filter_chars(string):
    filtered_string = ""
    for i, c in enumerate(string):
        if 259 <= i <= 502 and ',' <= c <= '3':
            continue
        filtered_string += c
    return filtered_string
