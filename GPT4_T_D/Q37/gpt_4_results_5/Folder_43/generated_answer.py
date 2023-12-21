
def filter_chars(input_string):
    to_remove = [x for x in input_string[15:56] if 'W' <= x <= '{']
    result_string = "".join([char for char in input_string if char not in to_remove])
    return result_string
