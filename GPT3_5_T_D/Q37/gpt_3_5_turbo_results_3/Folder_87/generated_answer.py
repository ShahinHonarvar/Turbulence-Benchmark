
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 18 and i <= 81 and string[i] >= 'W' and string[i] <= '[':
            continue
        filtered_string += string[i]
    return filtered_string
