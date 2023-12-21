
def return_n_smallest_chars(string):
    ascii_chars = [char for char in string]
    ascii_chars.sort(key=lambda x: ord(x))
    top_36_chars = ascii_chars[:36]
    top_36_chars.sort(reverse=True)
    return top_36_chars
