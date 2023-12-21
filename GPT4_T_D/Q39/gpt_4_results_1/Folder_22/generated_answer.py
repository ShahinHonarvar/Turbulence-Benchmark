
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=ord, reverse=True)
    greatest_chars = sorted_chars[:76]
    return sorted(greatest_chars)
