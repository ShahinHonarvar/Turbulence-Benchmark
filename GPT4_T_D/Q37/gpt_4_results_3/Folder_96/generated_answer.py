
def filter_chars(my_string):
    for ch in my_string[86:93]:
        if '!' <= ch <= 's':
            my_string = my_string.replace(ch, '', 1)
    return my_string
