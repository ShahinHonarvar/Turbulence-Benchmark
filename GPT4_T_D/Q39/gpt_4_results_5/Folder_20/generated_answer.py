
def return_n_greatest_chars(str_chars):
    str_sorted = sorted(str_chars, key=ord, reverse=True)
    greatest_chars = str_sorted[:40]
    sorted_greatest_chars = sorted(greatest_chars)
    return sorted_greatest_chars
