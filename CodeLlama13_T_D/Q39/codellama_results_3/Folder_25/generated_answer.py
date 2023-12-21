
def return_n_greatest_chars(string):
    chars = set(string)
    sorted_chars = sorted(chars, key=ord, reverse=True)[:29]
    return sorted_chars
