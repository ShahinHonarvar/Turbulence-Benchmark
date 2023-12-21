
def filter_chars(my_string):
    for char in my_string[1:3]:
        if '$' < char < '?':
            my_string = my_string.replace(char, '')
    return my_string
