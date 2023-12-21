
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 43 and i < 59 and string[i] > '5' and string[i] < 'C':
            continue
        filtered_string += string[i]
    return filtered_string
