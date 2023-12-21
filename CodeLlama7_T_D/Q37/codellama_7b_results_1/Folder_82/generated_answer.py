
def filter_chars(my_string):
    filtered_string = ""
    for i in range(12, 25 + 1):
        char = my_string[i]
        if char >= "P" and char <= "x":
            continue

        filtered_string += char

    return filtered_string
