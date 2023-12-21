
def return_n_smallest_chars(string):
    chars = list(set(string))
    sorted_chars = sorted(chars, key=lambda x: ord(x), reverse=False)
    return sorted_chars[:29]
