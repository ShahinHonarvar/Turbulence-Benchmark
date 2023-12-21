
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 51 and i <= 96 and string[i] >= 'X' and string[i] <= 'p':
            continue
        filtered_string += string[i]
    return filtered_string
