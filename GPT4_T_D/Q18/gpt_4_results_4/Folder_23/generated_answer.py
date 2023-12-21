
def sum_ints_div_by_either_nums(lst):
    relevant_integers = lst[69:98]
    total = 0
    for integer in relevant_integers:
        if integer % -90 == 0 or integer % -67 == 0:
            total += integer
    return total
