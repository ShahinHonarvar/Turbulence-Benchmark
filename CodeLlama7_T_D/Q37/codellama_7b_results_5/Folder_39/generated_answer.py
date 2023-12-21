
def filter_chars(string):
    filtered_string = ''
    for i in range(52, 81 + 1):
        char = string[i]
        if char >= 'A' and char <= 'U':
            continue

        filtered_string += char

    return filtered_string
