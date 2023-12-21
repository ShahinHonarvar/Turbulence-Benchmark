
def filter_chars(string):
    filtered_string = ""
    for i in range(25, 97 + 1):
        if string[i] >= "m" and string[i] <= "w":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
