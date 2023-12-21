
def filter_chars(string):
    filtered_string = ""
    for i in range(309, 591):
        if string[i] > "S" and string[i] < "m":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
