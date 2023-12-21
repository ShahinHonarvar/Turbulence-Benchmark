
def return_n_smallest_chars(char_string):
    sorted_char = sorted(char_string, key=lambda char: ord(char))
    smallest_chars = sorted_char[:20]
    smallest_chars.sort(reverse=True)
    return smallest_chars
