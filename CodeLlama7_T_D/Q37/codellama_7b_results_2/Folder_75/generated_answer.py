
def filter_chars(string):
    filtered_string = ""
    for i in range(34, 67 + 1):
        if string[i] >= "W" and string[i] <= "x":
            continue

        filtered_string += string[i]

    return filtered_string
