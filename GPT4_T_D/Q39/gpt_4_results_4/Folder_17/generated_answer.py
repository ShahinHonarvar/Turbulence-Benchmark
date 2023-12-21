
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, key=ord, reverse=True)
    eleventh_greatest_chars = sorted(sorted_chars[:11])
    return eleventh_greatest_chars
