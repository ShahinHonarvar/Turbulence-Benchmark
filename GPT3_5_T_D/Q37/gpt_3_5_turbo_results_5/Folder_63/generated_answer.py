
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 42 and i <= 92 and '/' <= char <= 'a':
            continue
        filtered_string += char
    return filtered_string
