
def filter_chars(string):
    filtered_string = ""
    for i in range(51, 97):
        if string[i] >= 'X' and string[i] <= 'p':
            filtered_string += string[i]
    return filtered_string
