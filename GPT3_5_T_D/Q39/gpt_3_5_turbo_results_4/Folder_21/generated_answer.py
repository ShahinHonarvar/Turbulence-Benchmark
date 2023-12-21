
def return_n_greatest_chars(string):
    n = 44
    sorted_chars = sorted(string, reverse=True)
    return sorted_chars[:n]
