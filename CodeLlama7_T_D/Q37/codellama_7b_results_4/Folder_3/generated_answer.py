 def filter_chars(my_string):
    filtered_string = ""
    for i in range(37, 56 + 1):
        if my_string[i] >= "6" and my_string[i] <= "_":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
