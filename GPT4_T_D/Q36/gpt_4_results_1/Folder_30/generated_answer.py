
def filter_chars(my_str):
    for char in my_str[24:45]:
        if '3' < char < 'I':
            my_str = my_str.replace(char, "")
    return my_str
