
def return_n_greatest_chars(s):
    s_list = list(s)
    s_list.sort(key = ord, reverse = True)
    s_list = s_list[:66]
    s_list.sort(key = ord)
    return s_list
