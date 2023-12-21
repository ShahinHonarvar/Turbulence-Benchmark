
def filter_chars(string):
    filtered_string = ""
    for i in range(19, 90 + 1):
        if string[i] >= "F" and string[i] <= "h":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
