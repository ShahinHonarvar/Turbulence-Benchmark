
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)
    greatest_chars = sorted_chars[:45]
    greatest_chars.sort()
    return greatest_chars
