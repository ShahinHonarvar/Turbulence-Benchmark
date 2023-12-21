
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if (i >= 41) and (i <= 86) and (string[i] >= 'S') and (string[i] <= 's'):
            string = string.replace(string[i], '')
    filtered_string = string
    return filtered_string
