
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=lambda x: ord(x))
    return sorted_chars[:36][::-1]
