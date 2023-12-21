
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:45]
    smallest_chars.sort(reverse=True)
    return smallest_chars
