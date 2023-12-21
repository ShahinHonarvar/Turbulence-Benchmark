
def return_n_smallest_chars(s):
    s_list = list(s)
    s_list.sort(key=ord)
    s_list = s_list[:75]
    s_list.sort(reverse=True)
    return(s_list)
