
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 502 <= i < 946 and 'W' < string[i] < 'y':
            continue
        filtered_string += string[i]
    return filtered_string
