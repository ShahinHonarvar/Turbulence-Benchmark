
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 348 or i > 852 or string[i] < 'J' or string[i] > 'b':
            filtered_string += string[i]
    return filtered_string
