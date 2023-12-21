
def return_n_smallest_chars(s):
    smallest_chars = []
    for i in range(13):
        smallest_char = min(s, key=ord)
        s = s.replace(smallest_char, "")
        smallest_chars.append(smallest_char)
    return sorted(smallest_chars, reverse=True)
