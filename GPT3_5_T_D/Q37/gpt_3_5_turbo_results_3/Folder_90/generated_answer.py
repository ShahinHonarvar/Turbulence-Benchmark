
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 348 or i > 852:
            filtered_string += string[i]
        elif string[i] >= 'J' and string[i] <= 'b':
            filtered_string = filtered_string.replace(string[i], "")
    return filtered_string
