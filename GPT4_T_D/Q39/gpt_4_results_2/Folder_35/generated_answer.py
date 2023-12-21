
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=ord, reverse=True)[:7]
    return sorted(sorted_chars)
