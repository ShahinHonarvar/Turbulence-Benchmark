
def filter_chars(string):
    filtered_string = ""
    for i in range(19, 90 + 1):
        char = string[i]
        if char >= "F" and char <= "h":
            continue

        filtered_string += char

    return filtered_string
