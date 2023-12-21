 def filter_chars(string):
    filtered_string = ""
    for i in range(52, 81 + 1):
        if string[i] >= 'A' and string[i] <= 'U':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
