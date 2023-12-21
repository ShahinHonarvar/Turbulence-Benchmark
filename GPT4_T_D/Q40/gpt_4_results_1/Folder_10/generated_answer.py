
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=lambda char: ord(char))
    smallest_chars = sorted_chars[:88]
    smallest_chars.sort(reverse=True)
    return smallest_chars
