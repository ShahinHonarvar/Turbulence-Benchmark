
def filter_chars(string):
    filtered_string = ""
    for i in range(54, 63):
        if string[i] >= ")" and string[i] <= "9":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
