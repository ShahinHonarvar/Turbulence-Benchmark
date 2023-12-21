
def filter_chars(string):
    start_index = 73
    end_index = 74
    filter_chars = string[start_index:end_index + 1]
    filtered_string = string.replace(filter_chars, '')
    return filtered_string
