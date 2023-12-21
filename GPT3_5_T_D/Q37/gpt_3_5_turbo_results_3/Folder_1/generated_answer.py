
def filter_chars(string):
    start = 41
    end = 79
    filtered_string = ""
    for index, char in enumerate(string):
        if start <= index <= end and 'f' <= char <= '|':
            continue
        filtered_string += char
    return filtered_string
