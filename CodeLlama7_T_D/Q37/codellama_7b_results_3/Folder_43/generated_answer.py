
def filter_chars(string):
    filtered_string = ""
    for i in range(15, len(string)):
        if string[i] >= "W" and string[i] <= "{":
            continue
        else:
            filtered_string += string[i]
    return filtered_string
