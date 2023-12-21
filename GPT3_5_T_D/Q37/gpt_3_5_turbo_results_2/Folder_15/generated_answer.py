
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 2 or i > 6 or string[i] < '?' or string[i] > 'f':
            filtered_string += string[i]
    return filtered_string
