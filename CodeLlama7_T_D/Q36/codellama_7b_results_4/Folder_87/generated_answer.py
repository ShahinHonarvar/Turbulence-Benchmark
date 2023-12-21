
def filter_chars(my_string):
    filtered_string = ""
    for i in range(32, 61):
        if my_string[i] > '3' and my_string[i] < 'D':
            filtered_string += my_string[i + 1:]
    return filtered_string
