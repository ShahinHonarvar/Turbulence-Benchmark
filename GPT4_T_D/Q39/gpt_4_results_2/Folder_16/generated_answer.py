
def return_n_greatest_chars(s):
    s_list = sorted(s, reverse=True)
    greatest_chars = s_list[:64]
    return greatest_chars
