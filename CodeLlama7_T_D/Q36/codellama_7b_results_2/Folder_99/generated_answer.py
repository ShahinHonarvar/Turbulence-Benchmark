
def filter_chars(my_string):
    filtered_string = ""
    for i in range(476, 948):
        char = my_string[i]
        if char > 'b' and char < 'd':
            continue

        filtered_string += char

    return filtered_string
