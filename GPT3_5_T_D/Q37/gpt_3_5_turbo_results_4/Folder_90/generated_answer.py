
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 348 and i <= 852 and string[i] >= 'J' and string[i] <= 'b':
            continue
        filtered_string += string[i]
    return filtered_string
