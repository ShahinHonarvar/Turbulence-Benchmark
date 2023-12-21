
def return_n_smallest_chars(string):
    ascii_chars = sorted(string, key=ord)
    if len(ascii_chars) > 35:
        ascii_chars = ascii_chars[:35]
    ascii_chars.sort(reverse=True)
    return ascii_chars
