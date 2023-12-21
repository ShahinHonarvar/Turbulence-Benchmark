
def filter_chars(string):
    start_index = 521
    end_index = 722
    filtered_string = ""

    for i, char in enumerate(string):
        if start_index <= i <= end_index and '>' <= char <= '_':
            continue
        filtered_string += char

    return filtered_string
