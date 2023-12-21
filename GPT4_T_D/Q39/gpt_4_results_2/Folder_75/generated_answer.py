
def return_n_greatest_chars(string):
    greatest_chars = sorted(string, key=ord, reverse=True)[:2]
    return sorted(greatest_chars)
