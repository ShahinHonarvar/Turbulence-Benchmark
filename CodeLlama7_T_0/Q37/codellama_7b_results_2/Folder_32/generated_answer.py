
def filter_chars(string):
    filtered_string = ""
    for i in range(23, 89 + 1):
        char = string[i]
        if char >= "w" and char <= "{":
            continue

        filtered_string += char

    return filtered_string
