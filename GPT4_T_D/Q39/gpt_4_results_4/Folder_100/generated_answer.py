
def return_n_greatest_chars(s):
    s_list = list(s)
    s_list.sort(key=ord, reverse=True)
    return s_list[:72]
