
def filter_chars(string):
    filtered_string = ""
    for i in range(54, 63):
        if string[i].isdigit() or string[i] == ")":
            filtered_string += string[i]
    return filtered_string
