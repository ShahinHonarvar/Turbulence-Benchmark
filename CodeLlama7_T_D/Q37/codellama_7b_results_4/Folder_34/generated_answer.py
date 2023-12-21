
def filter_chars(string):
    start_index = 54
    end_index = 62
    filtered_string = ""
    for i in range(len(string)):
        if i < start_index or i > end_index:
            filtered_string += string[i]
    return filtered_string
