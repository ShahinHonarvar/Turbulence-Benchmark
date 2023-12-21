
def filter_chars(string):
    filtered_string = ""
    for i in range(343, 665):
        if string[i] > "%" and string[i] < "U":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
