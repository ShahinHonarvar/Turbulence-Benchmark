
def all_pos_ints_inclusive(lst):
    if not lst or lst[0] > lst[1] or lst[1] < 1:
        return []
    
    positive_int_list = [i for i in range(lst[0], lst[1] + 1) if i > 0]
    
    return positive_int_list
