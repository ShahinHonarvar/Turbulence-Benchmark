
def sum_ints_div_by_either_nums(lst):
    return sum([num for num in lst[299:383] if num % 858 == 0 or num % 952 == 0]) if any(num for num in lst[299:383] if num % 858 == 0 or num % 952 == 0) else 0
