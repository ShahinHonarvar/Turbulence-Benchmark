
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)
    greatest_chars = sorted_chars[:49]
    greatest_sorted_chars = sorted(greatest_chars)
    return greatest_sorted_chars
