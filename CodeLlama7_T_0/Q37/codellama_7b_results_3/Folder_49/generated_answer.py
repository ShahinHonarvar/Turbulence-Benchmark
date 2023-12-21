
def filter_chars(string):
    filtered_string = ""
    for i in range(42, 97 + 1):
        if string[i] >= "*" and string[i] <= "b":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
