
def return_n_greatest_chars(chars):
    sorted_list = sorted(chars, key=ord, reverse=True)
    return sorted_list[:23]
