
def filter_chars(string):
    start_index = 515
    end_index = 538
    filtered_string = ""
    for index, char in enumerate(string):
        if start_index <= index <= end_index and '+' <= char <= '}':
            continue
        filtered_string += char
    return filtered_string
