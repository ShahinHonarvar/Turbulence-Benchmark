
def filter_chars(my_string):
    for char in my_string[310:591]:
        if 'S' < char < 'm':
            my_string = my_string.replace(char, '')
    return my_string
