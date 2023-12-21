
def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for num in lst[58:82]:
        if num % 55 == 0 and num % 10 == 0:
            divisible_ints.append(num)
    return divisible_ints
