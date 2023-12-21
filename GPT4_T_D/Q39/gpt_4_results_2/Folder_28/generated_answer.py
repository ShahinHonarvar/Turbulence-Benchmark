
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=ord, reverse=True)
    return sorted(sorted_chars[:3])
