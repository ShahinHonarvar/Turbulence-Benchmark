
def filter_chars(string):
    filtered_string = ""
    for i in range(36, 80):
        if string[i] >= "a" and string[i] <= "i":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
