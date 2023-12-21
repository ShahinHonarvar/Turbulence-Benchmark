
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 38 and i <= 99:
            if string[i] >= 'A' and string[i] <= 'Q':
                continue
        filtered_string += string[i]
    return filtered_string
