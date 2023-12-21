
def filter_chars(string):
    filtered_string = ""
    for i in range(61, 71):
        if string[i] >= '0' and string[i] <= '@':
            filtered_string += string[i]
    return filtered_string
