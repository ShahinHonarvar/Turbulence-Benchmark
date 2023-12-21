
def filter_chars(string):
    start_index = 81
    end_index = 86

    filtered_string = ""
    for i, char in enumerate(string):
        if start_index <= i < end_index:
            if '!' < char < 's':
                continue
        filtered_string += char

    return filtered_string
