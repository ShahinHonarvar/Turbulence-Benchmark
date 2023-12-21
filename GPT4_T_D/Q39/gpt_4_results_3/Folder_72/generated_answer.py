
def return_n_greatest_chars(chars):
    sorted_chars = sorted(list(chars), key=ord, reverse=True)
    return sorted_chars[:37]
