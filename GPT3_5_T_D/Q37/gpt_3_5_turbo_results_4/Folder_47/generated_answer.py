
def filter_chars(string):
    start_index = 38
    end_index = 54
    for i in range(start_index, end_index + 1):
        if ':' <= string[i] <= 'r':
            string = string.replace(string[i], '')
    return string
