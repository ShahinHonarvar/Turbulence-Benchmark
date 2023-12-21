
def filter_chars(string):
    start_index = 54
    end_index = 83
    filtered_string = ""

    for index, char in enumerate(string):
        if start_index <= index <= end_index and 'j' <= char <= 'v':
            continue
        filtered_string += char

    return filtered_string
