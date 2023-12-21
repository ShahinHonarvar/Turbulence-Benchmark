
def return_n_greatest_chars(s):
    s_list = list(s)
    s_list.sort(reverse=True)
    return sorted(s_list[:5])
