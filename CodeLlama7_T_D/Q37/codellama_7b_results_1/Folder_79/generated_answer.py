
def filter_chars(my_string):
    filtered_string = ""
    for i in range(len(my_string)):
        char = my_string[i]
        if (char >= '@' and char <= 'T') and (i < 10 or i > 52):
            filtered_string += char

    return filtered_string
