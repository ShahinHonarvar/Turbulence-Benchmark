
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 52 and i <= 81 and string[i] >= 'A' and string[i] <= 'U':
            continue
        filtered_string += string[i]
    return filtered_string
