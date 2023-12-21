
def filter_chars(my_string):
    for char in my_string[32:70]:
        if 'B' < char < 'v':
            my_string = my_string.replace(char, '')
    return my_string
