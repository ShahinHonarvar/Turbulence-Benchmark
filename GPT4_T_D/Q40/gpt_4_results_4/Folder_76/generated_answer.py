
def return_n_smallest_chars(string):
    sorted_chars = sorted(string[:3], key=ord, reverse=True)
    return sorted_chars
