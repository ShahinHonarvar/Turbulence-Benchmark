
def filter_chars(string):
    filtered_string = string[:521] + string[722+1:]
    for i in range(521, 722+1):
        if '>' <= string[i] <= '_':
            filtered_string = filtered_string.replace(string[i], '')
    return filtered_string
