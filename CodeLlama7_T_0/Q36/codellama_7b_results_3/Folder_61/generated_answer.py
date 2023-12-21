
def filter_chars(string):
    filtered_string = ""
    for i in range(3, 10):
        if string[i] > '*' and string[i] < 'E':
            filtered_string += string[:i] + string[i+1:]
    return filtered_string
