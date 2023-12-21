
def filter_chars(my_string):
    for char in my_string[32:50]:
        if '/' < char < 'J':
            my_string = my_string.replace(char, '')
    return my_string
