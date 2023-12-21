
def filter_chars(string):
    filtered_string = string[0]
    for i in range(1, len(string)):
        if i > 1 and i < 7:
            if string[i] > '3' and string[i] < '^':
                filtered_string = filtered_string.replace(string[i], "")
        else:
            filtered_string += string[i]
    return filtered_string
