
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[:2]
    total = 0
    for num in subset:
        if num % 1 == 0 or num % 2 == 0:
            total += num
    return total
