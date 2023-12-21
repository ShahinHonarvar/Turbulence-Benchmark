
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)
    greatest_chars = sorted_chars[:45]
    return sorted(greatest_chars)
