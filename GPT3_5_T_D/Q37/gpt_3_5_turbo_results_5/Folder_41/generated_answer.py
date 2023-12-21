
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 26 or i > 64:
            filtered_string += string[i]
        elif string[i] < 'V' or string[i] > 'o':
            filtered_string += string[i]
    return filtered_string
