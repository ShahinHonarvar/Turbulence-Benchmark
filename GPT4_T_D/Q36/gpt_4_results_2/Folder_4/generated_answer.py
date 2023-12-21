
def filter_chars(my_string):
    for char in my_string[43:67]:
        if '6' < char < 'g':
            my_string = my_string.replace(char, '')
    return my_string
