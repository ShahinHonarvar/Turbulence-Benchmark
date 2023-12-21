
def return_n_smallest_chars(string):
    chars = []
    for i in range(32):
        smallest_char = min(string, key=ord)
        string = string.replace(smallest_char, "")
        chars.append(smallest_char)
    return chars
