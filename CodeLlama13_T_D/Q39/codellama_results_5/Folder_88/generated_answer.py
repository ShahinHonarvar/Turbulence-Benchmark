
def return_n_greatest_chars(string):
    chars = set(string)
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[-84:]
