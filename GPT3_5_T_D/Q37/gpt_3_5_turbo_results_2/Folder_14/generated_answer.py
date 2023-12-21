
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 35 and i <= 98 and string[i] >= 'A' and string[i] <= 'b':
            continue
        filtered_string += string[i]
    return filtered_string
