
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    for i in range(len(string)):
        if (string[i] >= '9' and string[i] <= 'w') and (i >= 503 and i <= 753):
            continue

        else:
            filtered_string += string[i]

    return filtered_string
