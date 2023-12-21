
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True, key=lambda c: ord(c))
    return sorted_chars[:37]
