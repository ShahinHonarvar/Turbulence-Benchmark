
def filter_chars(string):
    filtered_string = ""
    for i in range(515, 539):
        if string[i] >= "+" and string[i] <= "}":
            continue
        else:
            filtered_string += string[i]
    return filtered_string
