
def filter_chars(string):
    filtered_string = ""
    for i in range(36, 80):
        if string[i].isalpha() and string[i].lower() >= 'a' and string[i].lower() <= 'i':
            continue

        else:

            filtered_string += string[i]

    return filtered_string
