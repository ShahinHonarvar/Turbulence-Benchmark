
def filter_chars(my_string):
    for char in my_string[33:61]:
        if '3' < char < 'D':
            my_string = my_string.replace(char, '')
    return my_string
