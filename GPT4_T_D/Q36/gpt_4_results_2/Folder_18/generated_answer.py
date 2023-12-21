
def filter_chars(my_string):
    chars_to_remove = set()
    for i in range(588, 648):
        if i < len(my_string):
            char = my_string[i]
            if ',' < char < 'c':
                chars_to_remove.add(char)
    for char_to_remove in chars_to_remove:
        my_string = my_string.replace(char_to_remove, '')
    return my_string
