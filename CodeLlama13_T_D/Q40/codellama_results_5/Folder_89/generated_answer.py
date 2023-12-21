
def return_n_smallest_chars(s):
    char_ascii = {c: ord(c) for c in s}
    n_smallest_chars = sorted(char_ascii, key=lambda x: char_ascii[x])[:55]
    return ''.join(n_smallest_chars)
