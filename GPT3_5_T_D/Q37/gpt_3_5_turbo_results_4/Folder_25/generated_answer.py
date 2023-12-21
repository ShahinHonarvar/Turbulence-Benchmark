
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 31 and i <= 38:
            if string[i] >= ';' and string[i] <= 'g':
                continue
        filtered_string += string[i]
    return filtered_string
