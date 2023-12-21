
def filter_chars(my_string):
    to_remove = []
    for i in range(max(0, 37), min(57, len(my_string))):
        if '6' <= my_string[i] <= '_':
            to_remove.append(my_string[i])
    for char in set(to_remove):
        my_string = my_string.replace(char, '')
    return my_string
