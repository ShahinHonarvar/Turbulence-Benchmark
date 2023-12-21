
def filter_chars(string):
    filtered_string = ""
    for i in range(3, 8):
        if string[i] > "?" and string[i] < "k":
            filtered_string += string[:i] + string[i+1:]
    return filtered_string
