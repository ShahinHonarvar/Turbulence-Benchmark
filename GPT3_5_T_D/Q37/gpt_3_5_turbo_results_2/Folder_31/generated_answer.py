
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 57 and i <= 96:
            if string[i] >= '<' and string[i] <= 'w':
                filtered_string += string[i]
        else:
            filtered_string += string[i]
    return filtered_string
