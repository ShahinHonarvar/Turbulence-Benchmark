
def filter_chars(string):
    filtered_string = ""
    for i in range(2, len(string)):
        if string[i] >= "?" and string[i] <= "f":
            continue
        else:
            filtered_string += string[i]
    return filtered_string
