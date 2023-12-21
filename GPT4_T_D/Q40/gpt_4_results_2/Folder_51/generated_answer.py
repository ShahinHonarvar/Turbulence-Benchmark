
def return_n_smallest_chars(char_string):
    sorted_string = sorted(char_string, key=ord)
    asc_list = sorted_string[:45]
    return asc_list[::-1]
