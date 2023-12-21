
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    for i in range(3, len(string)):
        if string[i] > "?" and string[i] < "k":
            continue

        filtered_string += string[i]

    return filtered_string
