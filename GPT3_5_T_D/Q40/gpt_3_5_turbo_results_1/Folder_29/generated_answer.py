
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=lambda c: ord(c))
    return sorted_chars[:23][::-1]
