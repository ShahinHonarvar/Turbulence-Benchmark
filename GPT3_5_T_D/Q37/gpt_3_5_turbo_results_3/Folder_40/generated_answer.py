
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 0 and i <= 1 and string[i] >= '*' and string[i] <= 's':
            continue
        else:
            filtered_string += string[i]
    return filtered_string
