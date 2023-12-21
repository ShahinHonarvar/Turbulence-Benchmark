
def sum_ints_div_by_either_nums(int_list):
    return sum(num for i,num in enumerate(int_list[11:47]) if num%55==0 or num%36==0)
