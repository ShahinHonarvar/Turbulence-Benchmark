
def filter_chars(string):
    filtered_string = ""
    for i in range(38, 81):
        if string[i] > "." and string[i] < "^":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
