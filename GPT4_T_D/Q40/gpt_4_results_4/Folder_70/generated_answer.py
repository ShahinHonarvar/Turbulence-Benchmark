
def return_n_smallest_chars(string):
    return sorted(sorted(string)[:2], reverse=True)
