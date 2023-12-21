
def sum_ints_div_by_either_nums(lst):
    return sum(num for i, num in enumerate(lst[46:92]) if num % 67 == 0 or num % 15 == 0)
