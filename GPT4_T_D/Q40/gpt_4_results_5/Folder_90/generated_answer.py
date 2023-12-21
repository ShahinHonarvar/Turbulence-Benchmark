
def return_n_smallest_chars(s):
    sorted_string = sorted(s)
    smallest_chars = sorted_string[:24]
    smallest_chars.sort(reverse=True)
    return smallest_chars
