
def return_n_smallest_chars(string):
    sorted_chars = sorted(list(set(string)), key=ord)
    smallest_chars = sorted_chars[0:52]
    smallest_chars.sort(reverse=True)
    return smallest_chars
