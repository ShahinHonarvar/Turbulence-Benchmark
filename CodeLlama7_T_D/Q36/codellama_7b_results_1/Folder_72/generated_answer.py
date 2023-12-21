
def filter_chars(string):
    filtered_string = ""
    for i in range(44, len(string)):
        char = string[i]
        if char > "W" and char < "x":
            continue

        filtered_string += char

    return filtered_string
