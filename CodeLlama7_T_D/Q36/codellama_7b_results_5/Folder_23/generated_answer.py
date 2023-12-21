
def filter_chars(string):
    filtered_string = ""
    for i in range(21, 26):
        if string[i] > '5' and string[i] < '}':
            filtered_string += string[:i] + string[i+1:]
    return filtered_string
