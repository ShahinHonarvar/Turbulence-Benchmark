
def filter_chars(string):
    filtered_string = ""
    for i in range(3, len(string)):
        if string[i] > "Y" and string[i] < "s":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
