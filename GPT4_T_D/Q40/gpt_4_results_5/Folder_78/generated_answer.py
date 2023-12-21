
def return_n_smallest_chars(s):
    sorted_string = sorted(s, key=ord)
    smallest_chars_list = sorted_string[:43]
    smallest_chars_list.sort(reverse=True)
    return smallest_chars_list
