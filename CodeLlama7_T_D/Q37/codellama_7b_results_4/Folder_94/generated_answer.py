
def filter_chars(my_string):
    filtered_string = ""
    for i in range(51, 96 + 1):
        char = my_string[i]
        if char >= 'X' and char <= 'p':
            continue

        filtered_string += char

    return filtered_string
