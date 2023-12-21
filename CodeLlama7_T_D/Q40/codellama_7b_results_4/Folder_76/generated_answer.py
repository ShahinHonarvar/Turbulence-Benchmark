
def return_n_smallest_chars(string):
    smallest_chars = []
    for i in range(3):
        smallest_char = min(string, key=ord)
        smallest_chars.append(smallest_char)
        string = string.replace(smallest_char, '', 1)
    return sorted(smallest_chars, reverse=True)
