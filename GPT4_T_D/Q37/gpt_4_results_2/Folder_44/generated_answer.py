
def filter_chars(my_string):
    for char in my_string[21:44]:
        if '+' <= char <= '8':
            my_string = my_string.replace(char, '')
    return my_string
