
def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort(key=lambda x: ord(x))
    chars = chars[:23]
    chars.sort(reverse=True)
    return chars
