
def filter_chars(string):
    filtered_string = ""
    for i in range(77, 87):
        if string[i] > ";" and string[i] < "r":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
