
def return_n_smallest_chars(char_string):
    sorted_string = sorted(char_string)
    smallest_chars = sorted_string[:2]
    smallest_chars.sort(reverse=True)
    return smallest_chars
