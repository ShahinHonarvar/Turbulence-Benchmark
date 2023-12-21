
def filter_chars(my_string):
    range_string = my_string[41:87]
    for char in range_string:
        if 'S' <= char <= 's':
            my_string = my_string.replace(char, "")
    return my_string
