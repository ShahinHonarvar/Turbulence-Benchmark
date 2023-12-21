
def filter_chars(string):
    filtered_string = ""
    for i in range(29, 97 + 1):
        char = string[i]
        if char >= "-" and char <= "n":
            continue

        filtered_string += char

    return filtered_string
