
def filter_chars(string):
    filtered_string = ""
    for i in range(672, 709):
        if string[i] > 'X' and string[i] < '}':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
