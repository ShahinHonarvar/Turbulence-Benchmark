
def return_n_greatest_chars(s):
    chars_list = sorted(s, key=ord, reverse=True)[:87]
    return chars_list
