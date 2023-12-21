
def return_n_smallest_chars(chars_string):
    sorted_string = ''.join(sorted(chars_string))
    smallest_char_list = [char for char in sorted_string[:24]]
    return smallest_char_list
