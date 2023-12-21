
def return_n_smallest_chars(s):
    sorted_s = sorted(s)
    smallest_chars = sorted_s[0:88]
    smallest_chars.sort(reverse=True)
    return smallest_chars
