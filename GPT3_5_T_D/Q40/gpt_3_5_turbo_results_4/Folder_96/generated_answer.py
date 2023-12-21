
def return_n_smallest_chars(characters):
    smallest_chars = sorted(characters)[:20]
    smallest_chars.sort(reverse=True)
    return smallest_chars
