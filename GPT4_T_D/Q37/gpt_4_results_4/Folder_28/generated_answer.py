
def filter_chars(string):
    modified_set = set([char for index, char in enumerate(string) if 20 <= index <= 79 and '!' <= char <= 'T'])
    filtered_string = "".join([char for char in string if char not in modified_set])
    return filtered_string
