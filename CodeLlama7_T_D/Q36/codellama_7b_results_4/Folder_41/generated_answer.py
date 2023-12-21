
def filter_chars(my_string):
    # Replace all characters between 81 and 89 with an empty string
    for i in range(len(my_string)):
        if (i >= 81) and (i < 89):
            my_string = my_string.replace(my_string[i], "")
    return my_string
