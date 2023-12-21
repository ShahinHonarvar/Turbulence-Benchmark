 def filter_chars(my_string):
    filtered_string = ""
    for i in range(343, 665):
        if my_string[i] > "%" and my_string[i] < "U":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
