
def filter_chars(my_string):
    filtered_string = ""
    for char in my_string:
        if char == '_' or char == 'o':
            continue

        else:

            filtered_string += char

    return filtered_string
