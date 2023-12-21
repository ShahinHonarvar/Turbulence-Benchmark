
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 373 and i <= 901 and string[i] >= 'T' and string[i] <= 'h':
            continue
        else:
            filtered_string += string[i]
    return filtered_string
