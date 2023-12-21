
def return_n_smallest_chars(s):
    s = sorted(s)
    small_ascii_chars = s[:35]
    small_ascii_chars.sort(reverse=True)
    return small_ascii_chars
