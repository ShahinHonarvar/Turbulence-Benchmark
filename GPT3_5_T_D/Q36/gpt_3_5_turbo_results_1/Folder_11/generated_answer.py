
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 86 or i >= 93:
            filtered_string += string[i]
        elif string[i] > 'E' and string[i] < '~':
            continue
        else:
            filtered_string += string[i]
    return filtered_string
