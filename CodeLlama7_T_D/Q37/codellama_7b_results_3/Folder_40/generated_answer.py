
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        char = string[i]
        if char >= '*' and char <= 's':
            continue

        else:

            filtered_string += char

    return filtered_string
