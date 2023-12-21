
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 35 and i <= 89 and string[i] >= 'E' and string[i] <= 't':
            continue
        filtered_string += string[i]
    return filtered_string
