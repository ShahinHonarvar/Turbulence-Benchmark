
def filter_chars(my_string):
    for character in my_string[70:87]:
        if '#' < character < 'L':
            my_string = my_string.replace(character, '')
    return my_string
