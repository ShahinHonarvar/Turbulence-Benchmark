
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)
    smallest_89_chars = sorted_chars[:89]
    smallest_89_chars.sort(reverse=True)
    return smallest_89_chars
