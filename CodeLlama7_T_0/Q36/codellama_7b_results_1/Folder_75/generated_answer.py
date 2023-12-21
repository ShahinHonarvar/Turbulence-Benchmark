
def filter_chars(string):
    filtered_string = ""
    for i in range(46, 74):
        if string[i] > "&" and string[i] < "M":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
