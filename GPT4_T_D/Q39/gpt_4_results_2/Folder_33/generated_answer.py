
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)[:36]
    return sorted_chars
