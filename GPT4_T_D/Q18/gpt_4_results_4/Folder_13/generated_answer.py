
def sum_ints_div_by_either_nums(lst):
    result = [num for num in lst[13:19] if num % 45 == 0 or num % 20 == 0]
    return sum(result) if result else 0
