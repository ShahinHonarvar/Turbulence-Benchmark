
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:85]
    return smallest_chars[::-1]
