
def filter_chars(string):
    filtered_string = ""
    for i in range(513, 878):
        if string[i].isalpha() and string[i].lower() >= "?" and string[i].lower() <= "n":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
