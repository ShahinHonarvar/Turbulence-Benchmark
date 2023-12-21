
def filter_chars(my_str):
    indices_str = my_str[348:853]
    chars_to_remove = [char for char in indices_str if 'J' <= char <= 'b']
    for char in chars_to_remove:
        my_str = my_str.replace(char, "")
    return my_str
