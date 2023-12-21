
def sum_ints_div_by_either_nums(lst):
    return sum(n for n in lst[3:-1] if n%6==0 or n==1)
