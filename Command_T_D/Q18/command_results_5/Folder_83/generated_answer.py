
def sum_ints_div_by_either_nums(int_list):
    return sum(int(i) for i in int_list[90:200+1] if i%13==0 or i%31==0)
