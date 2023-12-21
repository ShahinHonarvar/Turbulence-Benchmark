
def return_n_greatest_chars(s):
    chars_list = sorted(s, key=ord)[:28]
    return chars_list
