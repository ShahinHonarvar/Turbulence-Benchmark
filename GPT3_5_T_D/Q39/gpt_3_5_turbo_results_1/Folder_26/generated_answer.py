
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=lambda x: -ord(x))
    return sorted_chars[:43]
