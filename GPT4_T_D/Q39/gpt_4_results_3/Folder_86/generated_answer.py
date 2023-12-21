
def return_n_greatest_chars(s):
    s_list = list(s)
    greatest_chars = sorted(s_list, key=ord, reverse=True)[:34]
    return sorted(greatest_chars)
