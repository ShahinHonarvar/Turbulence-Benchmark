
def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string), key=lambda x: ord(x))
    return sorted_chars[:19]
