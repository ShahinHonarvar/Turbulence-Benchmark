
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 384 and i <= 411 and '/' <= char <= '8':
            continue
        filtered_string += char
    return filtered_string
