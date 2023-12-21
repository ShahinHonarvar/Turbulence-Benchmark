 def filter_chars(string):
    filtered_string = ""
    for i in range(323, 526):
        if string[i] > ")" and string[i] < "O":
            continue

        else:

            filtered_string += string[i]

    return filtered_string
