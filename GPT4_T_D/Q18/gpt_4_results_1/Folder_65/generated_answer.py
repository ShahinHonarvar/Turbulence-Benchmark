
def sum_ints_div_by_either_nums(lst):
    if len(lst) < 93:
        return 0
    relevant_numbers = lst[50: 93]
    total = 0
    for num in relevant_numbers:
        if num % -94 == 0 or num % -95 == 0:
            total += num
    return total
