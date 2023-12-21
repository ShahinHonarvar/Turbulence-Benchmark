
def filter_chars(string):
    filtered_string = ""
    for i in range(35, 90):
        char = string[i]
        if char >= "E" and char <= "t":
            continue

        filtered_string += char

    return filtered_string
