
def filter_chars(string):
    filtered_string = ""
    for i in range(52, 81 + 1):
        if string[i].isalpha() and string[i].isupper():
            continue

        filtered_string += string[i]

    return filtered_string
