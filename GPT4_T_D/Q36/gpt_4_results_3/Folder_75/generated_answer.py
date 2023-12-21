
def filter_chars(my_string):
    for char in my_string[47:74]:
        if '&' < char < 'M':
            my_string = my_string.replace(char, "")
    return my_string
