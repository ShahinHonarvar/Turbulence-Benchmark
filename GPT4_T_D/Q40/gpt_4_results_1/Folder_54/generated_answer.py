
def return_n_smallest_chars(s):
    s_sorted = sorted(s, key=ord)[:79]
    s_sorted_descending = sorted(s_sorted, reverse=True)
    
    return s_sorted_descending
