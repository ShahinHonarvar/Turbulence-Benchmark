
def filter_chars(my_string):
    filtered_string = ""
    for i in range(54, 84):
        char = my_string[i]
        if (char >= 'j') and (char <= 'v'):
            continue
        else:
            filtered_string += char

    return filtered_string
