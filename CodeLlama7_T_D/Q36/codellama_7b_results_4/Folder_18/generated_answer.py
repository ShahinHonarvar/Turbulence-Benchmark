
def filter_chars(string):
    filtered_string = ""
    for i in range(587, 648):
        char = string[i]
        if char > ',' and char < 'c':
            continue

        else:

            filtered_string += char

    return filtered_string
