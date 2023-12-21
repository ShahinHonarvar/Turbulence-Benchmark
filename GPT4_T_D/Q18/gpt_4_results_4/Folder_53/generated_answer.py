
def sum_ints_div_by_either_nums(lst):
    if len(lst)<201:
        return 0
    else:
        divisible_by_17_or_minus_5 = [i for i in lst[200:201] if i%17 == 0 or i%-5 == 0]
        return sum(divisible_by_17_or_minus_5)
