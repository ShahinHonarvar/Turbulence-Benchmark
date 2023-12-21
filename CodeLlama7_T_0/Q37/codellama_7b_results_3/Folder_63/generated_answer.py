
def filter_chars(string):
    filtered_string = ""
    for i in range(42, 93):
        char = string[i]
        if char >= "/" and char <= "a":
            continue

        filtered_string += char

    return filtered_string
