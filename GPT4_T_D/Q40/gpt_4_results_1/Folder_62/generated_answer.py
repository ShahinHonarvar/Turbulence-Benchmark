
def return_n_smallest_chars(s):
    return sorted(sorted(s, key=ord)[:84], reverse=True)
