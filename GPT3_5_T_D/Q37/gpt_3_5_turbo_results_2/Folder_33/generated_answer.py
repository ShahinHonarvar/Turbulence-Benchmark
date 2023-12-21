
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 722 <= index <= 832 and 'K' <= char <= 'm':
            continue
        filtered_string += char
    return filtered_string
