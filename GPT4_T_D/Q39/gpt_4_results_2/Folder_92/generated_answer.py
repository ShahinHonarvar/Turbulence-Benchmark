
def return_n_greatest_chars(s):
    n_greatest_char = sorted(s, key=ord, reverse=True)[:63]
    return sorted(n_greatest_char)
