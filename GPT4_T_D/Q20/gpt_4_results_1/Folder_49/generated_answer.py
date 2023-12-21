
def find_n_th_smallest_num(lst):
    if len(lst) < 21 or len(lst) > 200:
        return "Error: List must have between 21 and 200 unique elements"
        
    sub_lst = sorted(lst[20:201])
    return sub_lst[10]
