
def filter_chars(string):
    filtered_string = ""
    for i in range(75, 100):
        if string[i] >= '8' and string[i] <= 'e':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
