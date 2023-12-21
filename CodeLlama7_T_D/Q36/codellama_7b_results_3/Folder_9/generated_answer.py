
def filter_chars(string):
    filtered_string = ""
    for i in range(50, 92):
        if string[i] > 'A' and string[i] < 'Q':
            filtered_string += string[:i] + string[i+1:]
    return filtered_string
