
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 24 and i <= 79 and string[i] >= 'a' and string[i] <= 'f':
            continue
        filtered_string += string[i]
    return filtered_string
