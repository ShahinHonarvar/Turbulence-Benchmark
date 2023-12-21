 def filter_chars(my_string):
    filtered_string = ""
    for i in range(71, 96 + 1):
        if my_string[i] >= "_" and my_string[i] <= "o":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
