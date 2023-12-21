
def filter_chars(string):
    start_index = 13
    end_index = 28
    filtered_string = ''

    for i in range(len(string)):
        if i >= start_index and i <= end_index and string[i] >= 'c' and string[i] <= 'n':
            continue
        filtered_string += string[i]

    return filtered_string
