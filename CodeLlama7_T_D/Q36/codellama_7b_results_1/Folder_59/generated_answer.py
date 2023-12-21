 def filter_chars(string):
    filtered_string = ""
    for i in range(3, 8):
        if string[i] > "?" and string[i] < "k":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
