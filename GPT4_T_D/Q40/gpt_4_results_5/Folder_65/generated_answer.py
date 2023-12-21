
def return_n_smallest_chars(char_string):
    sorted_string = sorted(char_string, key=ord)
    smallest_chars = sorted_string[:27]
    smallest_chars.reverse()
    return smallest_chars
