
def filter_chars(my_string):
    for char in my_string[45:48]:
        if '+' < char < 'l':
            my_string = my_string.replace(char, '')
    return my_string
