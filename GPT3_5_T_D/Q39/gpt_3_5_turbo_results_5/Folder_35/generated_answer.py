
def return_n_greatest_chars(string):
    n = 7
    sorted_chars = sorted(string, reverse=True)[:n]
    return sorted(sorted_chars)
