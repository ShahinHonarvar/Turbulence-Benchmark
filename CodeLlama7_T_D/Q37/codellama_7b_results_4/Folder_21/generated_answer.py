
def filter_chars(string):
    filtered_string = ''
    for i in range(603, 759 + 1):
        char = string[i]
        if char >= 'Q' and char <= 'h':
            continue

        filtered_string += char

    return filtered_string
