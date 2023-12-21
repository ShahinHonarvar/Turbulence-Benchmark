
def filter_chars(string):
    filtered_string = ""
    for i in range(28, 65 + 1):
        if string[i] >= "O" and string[i] <= "d":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
