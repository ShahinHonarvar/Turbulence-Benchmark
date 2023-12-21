
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 19 and i <= 92 and string[i] >= '8' and string[i] <= 'm':
            continue
        filtered_string += string[i]
    return filtered_string
