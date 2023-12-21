
def sum_ints_div_by_either_nums(lst):
    total = 0
    for value in lst[281:695]:
        if value % -722 == 0 or value % -731 == 0:
            total += value
    return total if total != 0 else 0
