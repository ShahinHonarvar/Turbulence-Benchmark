
def filter_chars(string):
    filtered_string = ""
    for i in range(27, 85 + 1):
        char = string[i]
        if char >= "!" and char <= "B":
            continue

        filtered_string += char

    return filtered_string
