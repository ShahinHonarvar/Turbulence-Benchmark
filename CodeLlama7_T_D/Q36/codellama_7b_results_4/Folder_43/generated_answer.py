
def filter_chars(string):
    filtered_string = ""
    for i in range(27, 75):
        if string[i] > "A" and string[i] < "i":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
