
def return_n_greatest_chars(s):
    ascii_list = sorted([char for char in s], key=lambda char: ord(char), reverse=True)[:31]
    return sorted(ascii_list)
