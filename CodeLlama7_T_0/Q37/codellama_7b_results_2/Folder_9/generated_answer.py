
def filter_chars(string):
    filtered_string = ""
    for i in range(38, 100):
        if string[i].isalpha() and string[i].isupper():
            continue

        else:

            filtered_string += string[i]

    return filtered_string
