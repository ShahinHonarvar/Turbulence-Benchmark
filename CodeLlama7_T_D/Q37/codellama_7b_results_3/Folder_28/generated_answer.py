
def filter_chars(my_string):
    filtered_string = ""
    for i in range(20, 80):
        char = my_string[i]
        if char >= "!" and char <= "T":
            continue

        filtered_string += char

    return filtered_string
