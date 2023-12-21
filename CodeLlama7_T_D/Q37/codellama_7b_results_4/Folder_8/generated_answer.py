
def filter_chars(string):
    filtered_string = ""
    for i in range(41, 87):
        if string[i].islower():
            filtered_string += string[i].upper()
        else:
            filtered_string += string[i]
    return filtered_string
