
def return_n_smallest_chars(my_string):
    char_list = sorted([char for char in my_string])
    return char_list[:3]
