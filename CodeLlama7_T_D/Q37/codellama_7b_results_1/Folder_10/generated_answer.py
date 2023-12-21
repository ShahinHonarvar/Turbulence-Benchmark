
def filter_chars(string):
    filtered_string = ""
    for i in range(63, 85):
        if string[i].isalpha() and string[i].islower():
            continue
        else:
            filtered_string += string[i]
    return filtered_string
