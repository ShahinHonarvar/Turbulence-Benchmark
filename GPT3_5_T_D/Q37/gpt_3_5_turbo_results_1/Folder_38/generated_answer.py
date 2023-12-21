
def filter_chars(string):
    filtered_str = ""
    for i, char in enumerate(string):
        if 24 <= i <= 79 and 'a' <= char <= 'f':
            continue
        filtered_str += char
    return filtered_str
