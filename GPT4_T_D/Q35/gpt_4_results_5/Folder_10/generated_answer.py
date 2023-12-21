
def remove_repeat_chars(my_string):
    substring = my_string[37:54]
    my_list = []
    for i in substring:
        if substring.count(i)>1:
            my_list.append(i)
    for char in my_list:
        my_string = my_string.replace(char, '')
    return my_string
