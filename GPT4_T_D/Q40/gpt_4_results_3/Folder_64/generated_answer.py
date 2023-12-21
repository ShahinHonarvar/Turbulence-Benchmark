
def return_n_smallest_chars(char_str):
    sorted_chars = sorted(char_str, key=ord)[:39]
    sorted_chars.sort(reverse=True)
    return sorted_chars
