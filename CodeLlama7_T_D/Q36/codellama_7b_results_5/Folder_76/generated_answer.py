
def filter_chars(my_string):
    # Create a new string with all characters removed
    filtered_string = ""

    for i in range(669, 888):
        # If the current character is between 'B' and 'Y' (exclusive), remove it from the string
        if my_string[i] > "B" and my_string[i] < "Y":
            continue

        else:

            filtered_string += my_string[i]

    return filtered_string
