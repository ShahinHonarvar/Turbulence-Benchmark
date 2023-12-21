
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    greatest_37_chars = sorted_chars[:37]
    return sorted(greatest_37_chars)
