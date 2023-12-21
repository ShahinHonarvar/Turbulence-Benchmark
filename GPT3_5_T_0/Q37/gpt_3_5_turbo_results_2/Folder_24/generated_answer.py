
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 36 and i <= 79 and string[i] >= '2' and string[i] <= 's':
            continue
        filtered_string += string[i]
    return filtered_string
