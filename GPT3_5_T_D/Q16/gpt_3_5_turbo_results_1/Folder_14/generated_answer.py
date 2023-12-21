
def sum_even_ints_inclusive(lst):
    even_nums = [num for num in lst[5:8] if num % 2 == 0]
    return sum(even_nums) if len(even_nums) > 0 else 0
