
def return_n_greatest_chars(chars):
    chars_list = list(chars)
    sorted_chars = sorted(chars_list, key=lambda x: ord(x))
    return sorted_chars[-82:]
