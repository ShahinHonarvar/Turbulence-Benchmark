
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)[:52]
    sorted_chars.sort()
    return sorted_chars
