
def filter_chars(input_string):
    filtered_string = input_string
    for chr_index in range(33, 61):
        if '3' < input_string[chr_index] < 'D':
            filtered_string = filtered_string.replace(input_string[chr_index], '')
    return filtered_string
