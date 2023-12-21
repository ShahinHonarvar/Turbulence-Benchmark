
def filter_chars(string):
    filtered_string = ""
    for i in range(41, 80):
        if string[i] >= "f" and string[i] <= "|":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
