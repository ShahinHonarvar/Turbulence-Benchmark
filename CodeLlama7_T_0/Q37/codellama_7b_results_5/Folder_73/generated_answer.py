
def filter_chars(string):
    filtered_string = ""
    for i in range(22, 86):
        char = string[i]
        if char >= '7' and char <= 'e':
            continue

        filtered_string += char

    return filtered_string
