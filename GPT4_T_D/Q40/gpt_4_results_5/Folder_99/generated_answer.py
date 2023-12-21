
def return_n_smallest_chars(s):
    sorted_char_list = sorted(s, key=lambda char: ord(char))
    n_smallest_chars = sorted_char_list[:35]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars
