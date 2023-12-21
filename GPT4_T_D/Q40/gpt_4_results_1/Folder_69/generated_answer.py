
def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s), key = lambda x: ord(x), reverse=False)
    while len(sorted_chars) < 65:
        sorted_chars += sorted_chars
    return sorted_chars[:65]
