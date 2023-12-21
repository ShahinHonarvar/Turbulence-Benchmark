
def filter_chars(my_string):
    filtered_string = ""
    for i in range(2, 6 + 1):
        if my_string[i - 1].isalpha() and my_string[i - 1].islower():
            continue

        else:
            filtered_string += my_string[i - 1]
    return filtered_string
