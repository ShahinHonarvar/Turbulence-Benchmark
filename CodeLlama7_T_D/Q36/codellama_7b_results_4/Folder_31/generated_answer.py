 def filter_chars(string):
    filtered_string = ""
    for i in range(14, len(string)):
        if string[i] > "9" and string[i] < "K":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
