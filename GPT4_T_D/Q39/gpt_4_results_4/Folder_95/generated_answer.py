
def return_n_greatest_chars(text):
    ascii_sorted = sorted(text, key=ord, reverse=True)
    return sorted(ascii_sorted[:36])
